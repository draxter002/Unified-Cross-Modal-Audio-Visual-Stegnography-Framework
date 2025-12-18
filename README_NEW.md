# 🔒 Unified Cross-Modal Audio-Visual Steganography Framework

A comprehensive steganography application that hides secret messages in images and audio files using LSB (Least Significant Bit) embedding techniques. Available as both a **desktop GUI application** and a **web application** that you can host online for free!

## ✨ Features

### 🖼️ Image Steganography
- Encode secret messages into PNG/BMP images using LSB substitution
- Decode hidden messages from stego-images
- Optional AES-256 encryption for extra security
- Visual comparison between original and stego-images
- Capacity calculation and validation

### 🎵 Audio Steganography
- Embed messages in WAV audio files using LSB technique
- Optional key-based embedding for enhanced security
- Waveform visualization before/after encoding
- Perfect audio quality preservation
- AES-256 encryption support

### 🌐 Web Interface (NEW!)
- Beautiful, modern web UI accessible from any device
- RESTful API for programmatic access
- Drag-and-drop file uploads
- Real-time capacity checking
- Download stego files directly
- Mobile-friendly responsive design

## 🚀 Quick Start

### Option 1: Run Web App Locally

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Start the web server:**
```bash
python app.py
```

3. **Open your browser:**
```
http://localhost:8000
```

### Option 2: Run Desktop GUI

```bash
python main_gui.py
```

## 🌍 Deploy to the Web (FREE!)

Your app is ready to deploy! I've set up configurations for multiple free hosting platforms:

### 🔥 Recommended: Render.com (Easiest)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Deploy! (Render auto-detects the `Procfile`)

**You'll get a free domain:** `https://your-app.onrender.com`

### 🚁 Alternative: Fly.io (Best Performance)

```bash
# Install Fly CLI
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Deploy
fly launch
fly deploy
```

### 🚂 Alternative: Railway.app

1. Go to [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Select your repo → Deploy!

**📖 Full deployment guide:** See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 📁 Project Structure

```
├── app.py                  # FastAPI web application
├── main_gui.py            # Tkinter desktop GUI
├── static/
│   └── index.html         # Web interface
├── modules/
│   ├── image_steg.py      # Image steganography logic
│   └── audio_steg.py      # Audio steganography logic
├── utils/
│   └── helpers.py         # Encryption & file utilities
├── tests/                 # Unit tests
├── Dockerfile             # Container configuration
├── Procfile              # Render deployment config
├── fly.toml              # Fly.io configuration
└── requirements.txt       # Python dependencies
```

## 🔧 Installation

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Desktop GUI Application
```bash
python main_gui.py
```

### Web Application
```bash
python app.py
```
Then visit `http://localhost:8000` in your browser.

### Python API Examples

#### Image Steganography
```python
from modules.image_steg import ImageSteganography

steg = ImageSteganography()

# Encode
success, msg = steg.encode_image("cover.png", "Secret message", "output.png")

# Decode
success, message = steg.decode_image("output.png")
print(message)  # "Secret message"
```

#### Audio Steganography
```python
from modules.audio_steg import AudioSteganography

steg = AudioSteganography()

# Encode with key
success, msg = steg.encode_audio("cover.wav", "Secret", "output.wav", key="mykey")

# Decode
success, message = steg.decode_audio("output.wav", key="mykey")
print(message)  # "Secret"
```

#### With Encryption
```python
from utils.helpers import EncryptionHelper

encrypt = EncryptionHelper()

# Encrypt message before hiding
encrypted = encrypt.encrypt_message("Secret", password="pass123")

# Encode encrypted message
steg.encode_image("cover.png", encrypted, "stego.png")

# Decode and decrypt
success, encrypted_msg = steg.decode_image("stego.png")
decrypted = encrypt.decrypt_message(encrypted_msg, password="pass123")
print(decrypted)  # "Secret"
```

## 🔌 REST API Endpoints

The web app provides a full REST API:

### Image Operations
- `POST /api/image/capacity` - Calculate image capacity
- `POST /api/image/encode` - Encode message in image
- `POST /api/image/decode` - Decode message from image

### Audio Operations
- `POST /api/audio/capacity` - Calculate audio capacity
- `POST /api/audio/encode` - Encode message in audio
- `POST /api/audio/decode` - Decode message from audio

### Example API Usage
```bash
# Calculate capacity
curl -X POST "http://localhost:8000/api/image/capacity" \
  -F "file=@cover.png"

# Encode message
curl -X POST "http://localhost:8000/api/image/encode" \
  -F "file=@cover.png" \
  -F "message=Secret text" \
  -F "use_encryption=true" \
  -F "password=mypass" \
  -o stego.png
```

## 🧪 Technical Details

### LSB Substitution
- **Images**: Modifies the least significant bit of each RGB pixel value
- **Audio**: Modifies the least significant bit of each audio sample
- **Key-based hiding**: Uses SHA-256 hash for deterministic random positioning

### Capacity Limits
- **Images**: (width × height × 3 channels) / 8 bytes
- **Audio**: (number of samples) / 8 bytes

### Security Features
- **AES-256 Encryption**: Optional encryption before embedding
- **Key-based Positioning**: Randomize bit positions with a secret key
- **SHA-256 Hashing**: Secure key derivation

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Individual test files:
```bash
python -m pytest tests/test_image.py
python -m pytest tests/test_audio.py
python -m pytest tests/test_utils.py
```

## 📦 Requirements

- Python 3.8+
- Pillow (image processing)
- NumPy (binary operations)
- SciPy (audio processing)
- PyCryptodome (encryption)
- FastAPI (web framework)
- Uvicorn (ASGI server)

## 🎨 Screenshots

### Web Interface
Modern, responsive design that works on desktop and mobile:
- Tabbed interface for Image and Audio operations
- Real-time capacity calculation
- Encryption options built-in
- Download results directly

### Desktop GUI
Full-featured Tkinter application with:
- Visual file selection
- Side-by-side comparison
- Waveform visualization
- Built-in encryption

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for learning or production!

## 👨‍💻 Author

Created as a comprehensive steganography demonstration project.

## 🔗 Resources

- **Live Demo**: Deploy to Render/Fly/Railway for free!
- **Documentation**: See [DEPLOYMENT.md](DEPLOYMENT.md)
- **API Docs**: Run the app and visit `/docs` for interactive API documentation

---

## 🎯 Next Steps

1. **Try it locally**: `python app.py` → Open `http://localhost:8000`
2. **Deploy for free**: Follow [DEPLOYMENT.md](DEPLOYMENT.md)
3. **Share your link**: Get a free domain on Render/Fly/Railway
4. **Add your custom domain**: All platforms support custom domains!

**Need help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
