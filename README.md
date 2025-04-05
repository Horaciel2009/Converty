# Converty - Media Format Converter

![Converty Banner](https://img.shields.io/badge/Converty-v1.2-8B5CF6)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Converty is a sleek, user-friendly web application for converting media files between different formats. Built with Flask and powered by FFmpeg and Pillow, it offers a modern dark-themed interface with an intuitive drag-and-drop upload system for both videos and images.

## 🎥 Features

- **Versatile Media Conversion**: 
  - **Video Formats**: Convert videos to popular formats (MP4, AVI, WebM, MKV, MOV, OGV)
  - **Image Formats**: Convert images between common formats (JPG, PNG, GIF, WebP, BMP, TIFF)
- **Intelligent Format Detection**: Automatically detects file type and offers appropriate conversion options
- **Multilingual Support**: Available in English and French
- **Modern Interface**: Dark-themed UI with intuitive controls
- **Drag-and-Drop Uploads**: Easy file selection
- **Responsive Design**: Works on desktop and mobile devices
- **Visual Progress Indication**: Progress bar during conversion

## 📋 Prerequisites

Before you start, make sure you have the following installed:

- Python 3.8 or higher
- FFmpeg (required for video processing)

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Horaciel2009/Converty.git
cd converty
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Install FFmpeg** (if not already installed)

- **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add to your PATH
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg` (Ubuntu/Debian) or `sudo dnf install ffmpeg` (Fedora)

## 🏁 Running the Application

1. **Start the Flask server**

```bash
python app.py
```

2. **Access the application**

Open your web browser and go to: http://127.0.0.1:5000

## 🔧 Configuration

The application creates two folders automatically:
- `uploads/`: Stores uploaded media files
- `converted/`: Stores converted media files

You can modify these paths in the `app.py` file if needed.

## 🌐 Language Support

Converty currently supports:
- English (default)
- French

The language can be changed using the language selector in the header.

## 🔍 How It Works

1. Upload your media file (image or video) by dragging and dropping it onto the upload area or clicking to browse
2. The application will automatically detect if it's an image or video
3. Select your desired output format from the dropdown menu (options will be based on your file type)
4. Click the "Convert" button to process the media file
5. Once conversion is complete, the file will automatically download

## 📝 Changelogs

### Version 1.2 (April 5, 2025)
- **Added image conversion support**:
  - Now supports converting between JPG, PNG, GIF, WebP, BMP and TIFF formats
  - Uses the Pillow library for high-quality image conversion
- **Improved UI/UX**:
  - Dynamic format selection menu that only appears after file selection
  - Intelligent format options that adapt to the selected file type
  - Clearer app flow with improved user guidance
- **Technical Improvements**:
  - Replaced deprecated 'imghdr' module with more robust file type detection
  - Added server-side verification of image files
  - Improved error handling for better user experience
  - Enhanced detection of file types through both extension and content analysis


### Version 1.1
- Added multilingual support (English and French)
- Improved error handling and messaging
- Enhanced mobile responsiveness

### Version 1.0
- Initial release with video conversion functionality
- Support for MP4, AVI, WebM, MKV, MOV, OGV formats
- Drag and drop interface
- Progress bar for conversion status

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Media Processing**: FFmpeg (video), Pillow (images)
- **Frontend**: HTML, CSS, JavaScript
- **Design**: Custom CSS inspired by Tailwind design principles

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ 

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

Made with Python & Flask