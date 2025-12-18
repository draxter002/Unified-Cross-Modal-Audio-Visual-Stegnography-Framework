# Steganography Analyzer

A comprehensive steganography application that hides secret messages in images and audio files using LSB (Least Significant Bit) embedding techniques.

## Features

### Image Steganography
- Encode secret messages into PNG images using LSB substitution
- Decode hidden messages from stego-images
- Visual comparison between original and stego-images
- Capacity calculation and validation

### Audio Steganography
- Embed messages in WAV audio files using LSB technique
- Optional key-based embedding for enhanced security
- Waveform visualization before/after encoding
- Perfect audio quality preservation

## Installation

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the GUI Application
```bash
python main_gui.py
```

### Image Steganography Example
```python
from modules.image_steg import encode_image, decode_image

# Encode
encode_image("cover.png", "Secret message", "output.png")

# Decode
message = decode_image("output.png")
print(message)  # "Secret message"
```

### Audio Steganography Example
```python
from modules.audio_steg import encode_audio, decode_audio

# Encode with optional key
encode_audio("cover.wav", "Secret data", "output.wav", key="mypassword")

# Decode with same key
message = decode_audio("output.wav", key="mypassword")
print(message)  # "Secret data"
```

## Technical Details

### LSB Substitution
- **Images**: Modifies the least significant bit of each RGB pixel value
- **Audio**: Modifies the least significant bit of each audio sample
- **Capacity**: Calculated based on file size and available bits

### Capacity Limits
- **Images**: (width × height × 3 channels) / 8 bytes
- **Audio**: (number of samples) / 8 bytes

## Project Structure
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

## Requirements
- Python 3.8+
- Pillow (image processing)
- NumPy (binary operations)
- SciPy (audio processing)
- PyCryptodome (encryption features)

## License
MIT License

## Author
Created as a comprehensive steganography demonstration project.
