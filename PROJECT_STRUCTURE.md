# Project Structure

```
Unified Cross Modal Audio-Visual Steganography Framework/
│
├── app.py                      # FastAPI web application (REST API)
├── main_gui.py                 # Tkinter desktop GUI application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── REFERENCE.md                # Additional references
├── .gitignore                  # Git ignore rules
│
├── modules/                    # Core steganography modules
│   ├── __init__.py
│   ├── audio_steg.py          # Audio steganography implementation
│   └── image_steg.py          # Image steganography implementation
│
├── utils/                      # Utility functions
│   ├── __init__.py
│   └── helpers.py             # Encryption and file helpers
│
├── static/                     # Web interface assets
│   └── index.html             # Web UI (HTML/CSS/JavaScript)
│
├── tests/                      # Unit tests
│   ├── test_audio.py          # Audio steganography tests
│   ├── test_image.py          # Image steganography tests
│   └── test_utils.py          # Utility function tests
│
├── run.bat                     # Windows run script
├── run.sh                      # Linux/Mac run script
│
├── Project Report.docx         # Project documentation
├── PROJECT_PRESENTATION.pdf    # Project presentation
│
├── test_audio.wav              # Sample audio file for testing
├── qwe.png                     # Sample image file
├── testlk.png                  # Sample image file
│
└── .venv/                      # Python virtual environment (generated)
```

## Key Components

### Core Files
- **`app.py`**: Web server using FastAPI, provides REST API endpoints
- **`main_gui.py`**: Desktop application with Tkinter GUI
- **`requirements.txt`**: All Python package dependencies

### Modules
- **`modules/audio_steg.py`**: LSB audio steganography with optional key-based positioning
- **`modules/image_steg.py`**: LSB image steganography for PNG/BMP files
- **`utils/helpers.py`**: AES-256 encryption, file operations, and helper functions

### Web Interface
- **`static/index.html`**: Single-page web application with modern UI

### Tests
- Unit tests for all core functionality using pytest

## How to Run

### Web Application
```bash
python app.py
# Visit http://localhost:8000
```

### Desktop GUI
```bash
python main_gui.py
```

### Run Tests
```bash
pytest tests/
```

## Installation

```bash
pip install -r requirements.txt
```

## Features

1. **Image Steganography**
   - Hide messages in PNG/BMP images using LSB
   - Calculate capacity
   - Optional AES-256 encryption

2. **Audio Steganography**
   - Hide messages in WAV audio files using LSB
   - Key-based random positioning
   - Optional AES-256 encryption

3. **Web Interface**
   - Modern, responsive design
   - Drag-and-drop file uploads
   - Real-time capacity checking
   - Download stego files

4. **Desktop GUI**
   - Visual file selection
   - Side-by-side comparison
   - Waveform visualization
   - Built-in encryption options
