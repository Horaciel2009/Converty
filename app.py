from flask import Flask, render_template, request, send_file, redirect, url_for, session, jsonify
import os
import ffmpeg
import subprocess
from PIL import Image  # Pour la conversion et la vérification d'images

app = Flask(__name__)
app.secret_key = "convertysecretkey"  # Nécessaire pour utiliser les sessions
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Types de fichiers supportés
VIDEO_EXTENSIONS = ['mp4', 'mov', 'avi', 'webm', 'mkv', 'ogv']
IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'tiff']

# Dictionnaires de traduction
translations = {
    'en': {
        'title': 'Converty - Media Converter',
        'header_title': 'Converty',
        'card_title': 'Convert a media file',
        'file_label': 'Media file',
        'file_placeholder': 'Drag and drop your media file here or click to browse',
        'format_label': 'Output format',
        'convert_button': 'Convert',
        'footer_text': 'Converty - Simple and fast media converter',
        'error_no_file': 'Please select a file',
        'error_conversion': 'Error during conversion:',
        'choose_language': 'Language',
        'video_file': 'Video file',
        'image_file': 'Image file'
    },
    'fr': {
        'title': 'Converty - Convertisseur Média',
        'header_title': 'Converty',
        'card_title': 'Convertir un fichier média',
        'file_label': 'Fichier média',
        'file_placeholder': 'Glisser-déposer votre fichier média ici ou cliquer pour parcourir',
        'format_label': 'Format de sortie',
        'convert_button': 'Convertir',
        'footer_text': 'Converty - Convertisseur de médias simple et rapide',
        'error_no_file': 'Veuillez sélectionner un fichier',
        'error_conversion': 'Erreur lors de la conversion:',
        'choose_language': 'Langue',
        'video_file': 'Fichier vidéo',
        'image_file': 'Fichier image'
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Définir la langue par défaut ou obtenir celle de la session
    if 'language' not in session:
        session['language'] = 'en'  # Anglais par défaut
    
    current_lang = session['language']
    translation = translations[current_lang]
    
    if request.method == 'POST':
        file = request.files['media']
        target_format = request.form['format']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            filename_no_ext = os.path.splitext(file.filename)[0]
            output_filename = f"{filename_no_ext}.{target_format}"
            output_path = os.path.join(CONVERTED_FOLDER, output_filename)
            
            # Détecter si c'est une vidéo ou une image
            file_ext = os.path.splitext(file.filename)[1].lower().replace('.', '')
            
            try:
                if file_ext in VIDEO_EXTENSIONS or file_ext not in IMAGE_EXTENSIONS:
                    # Conversion vidéo avec ffmpeg
                    input_stream = ffmpeg.input(filepath)
                    output_stream = ffmpeg.output(input_stream, output_path)
                    ffmpeg.run(output_stream, overwrite_output=True)
                else:
                    # Conversion d'image avec PIL
                    img = Image.open(filepath)
                    # Pour JPEG, spécifier la qualité
                    if target_format.lower() in ['jpg', 'jpeg']:
                        img.save(output_path, quality=90)
                    else:
                        img.save(output_path)
                
                return redirect(url_for('download_file', filename=output_filename))
            except Exception as e:
                error_message = f"{translation['error_conversion']} {str(e)}"
                return error_message
    return render_template('index.html', translation=translation)

@app.route('/change_language/<lang>')
def change_language(lang):
    if lang in translations:
        session['language'] = lang
    return redirect(url_for('index'))

@app.route('/detect_file_type', methods=['POST'])
def detect_file_type():
    """Détecte si le fichier est une image ou une vidéo et renvoie les formats disponibles"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Vérifier l'extension du fichier
    file_ext = os.path.splitext(file.filename)[1].lower().replace('.', '')
    
    # Vérification basée sur l'extension du fichier
    if file_ext in IMAGE_EXTENSIONS:
        try:
            # Vérification supplémentaire avec PIL pour confirmer que c'est bien une image
            img = Image.open(file)
            img.verify()  # Vérifie que le fichier est bien une image valide
            return jsonify({
                'type': 'image',
                'formats': IMAGE_EXTENSIONS
            })
        except Exception:
            # Si ce n'est pas une image valide, on traite comme vidéo par défaut
            return jsonify({
                'type': 'video',
                'formats': VIDEO_EXTENSIONS
            })
    else:
        # Par défaut, considérer comme vidéo
        return jsonify({
            'type': 'video',
            'formats': VIDEO_EXTENSIONS
        })

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(CONVERTED_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
