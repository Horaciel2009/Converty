# Converty - Video Format Converter

![Converty Banner](https://img.shields.io/badge/Converty-v1.0-8B5CF6)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Converty is a sleek, user-friendly web application for converting videos between different formats. Built with Flask and powered by FFmpeg, it offers a modern dark-themed interface with an intuitive drag-and-drop upload system.

## 🎥 Features

- **Simple Video Conversion**: Convert videos to popular formats (MP4, AVI, WebM, MKV, MOV, OGV)
- **Multilingual Support**: Available in English and French
- **Modern Interface**: Dark-themed UI with intuitive controls
- **Drag-and-Drop Uploads**: Easy file selection
- **Responsive Design**: Works on desktop like a charm!!
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
- `uploads/`: Stores uploaded video files
- `converted/`: Stores converted video files

You can modify these paths in the `app.py` file if needed.

## 🌐 Language Support

Converty currently supports:
- English (default)
- French

The language can be changed using the language selector in the header.

## 🔍 How It Works

1. Upload your video by dragging and dropping it onto the upload area or clicking to browse
2. Select your desired output format from the dropdown menu
3. Click the "Convert" button to process the video
4. Once conversion is complete, the file will automatically download

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Video Processing**: FFmpeg
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
