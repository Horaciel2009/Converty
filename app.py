from flask import Flask, render_template, request, send_file, redirect, url_for, session
import os
import ffmpeg
import subprocess

app = Flask(__name__)
app.secret_key = "convertysecretkey"  # Nécessaire pour utiliser les sessions
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Dictionnaires de traduction
translations = {
    'en': {
        'title': 'Converty - Video Converter',
        'header_title': 'Converty',
        'card_title': 'Convert a video',
        'file_label': 'Video file',
        'file_placeholder': 'Drag and drop your video file here or click to browse',
        'format_label': 'Output format',
        'convert_button': 'Convert',
        'footer_text': 'Converty - Simple and fast video converter',
        'error_no_file': 'Please select a video file',
        'error_conversion': 'Error during conversion:',
        'choose_language': 'Language'
    },
    'fr': {
        'title': 'Converty - Convertisseur Vidéo',
        'header_title': 'Converty',
        'card_title': 'Convertir une vidéo',
        'file_label': 'Fichier vidéo',
        'file_placeholder': 'Glisser-déposer votre fichier vidéo ici ou cliquer pour parcourir',
        'format_label': 'Format de sortie',
        'convert_button': 'Convertir',
        'footer_text': 'Converty - Convertisseur de vidéos simple et rapide',
        'error_no_file': 'Veuillez sélectionner un fichier vidéo',
        'error_conversion': 'Erreur lors de la conversion:',
        'choose_language': 'Langue'
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
        file = request.files['video']
        target_format = request.form['format']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            filename_no_ext = os.path.splitext(file.filename)[0]
            output_filename = f"{filename_no_ext}.{target_format}"
            output_path = os.path.join(CONVERTED_FOLDER, output_filename)
            
            # Conversion vidéo avec ffmpeg
            try:
                input_stream = ffmpeg.input(filepath)
                output_stream = ffmpeg.output(input_stream, output_path)
                ffmpeg.run(output_stream, overwrite_output=True)
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

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(CONVERTED_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
