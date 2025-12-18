# 🚀 QUICK REFERENCE CARD

## Installation (One-Time Setup)
```bash
pip install -r requirements.txt
python verify_installation.py
```

## Launch Application
```bash
python main_gui.py
# OR
run.bat          # Windows
./run.sh         # Linux/Mac
```

---

## Command Line Usage

### Image Steganography
```python
from modules.image_steg import encode_image, decode_image

# Encode
encode_image("cover.png", "Secret message", "stego.png")

# Decode
success, message = decode_image("stego.png")
print(message)
```

### Audio Steganography
```python
from modules.audio_steg import encode_audio, decode_audio

# Encode (with optional key)
encode_audio("cover.wav", "Secret", "stego.wav", key="password")

# Decode (use same key)
success, message = decode_audio("stego.wav", key="password")
print(message)
```

### Video Steganography
```python
from modules.video_steg import encode_video, decode_video

# Encode (modes: "frames", "audio", "both")
encode_video("video.mp4", "Message", "stego.mp4", mode="both")

# Decode
success, message = decode_video("stego.mp4", mode="both")
print(message)
```

---

## GUI Workflow

### Image Tab
1. Click "Select Cover Image" → Choose PNG
2. Enter secret message
3. (Optional) Enable encryption + enter password
4. Click "Encode Message" → Save stego-image
5. To decode: Click "Decode Message" → Select stego-image

### Audio Tab
1. Click "Select Audio File" → Choose WAV
2. Enter secret message
3. (Optional) Enter embedding key
4. Click "Encode Message" → Save stego-audio
5. To decode: Use same key if one was set

### Video Tab
1. Click "Select Video File" → Choose MP4/AVI
2. Select mode: Frames / Audio / Both
3. Enter secret message
4. (Optional) Enter key for audio
5. Click "Encode Message" → Wait (can be slow)
6. To decode: Use same mode and key

---

## File Format Cheat Sheet

| Format | Use Case | Status |
|--------|----------|--------|
| PNG | Images | ✅ Perfect (lossless) |
| JPG | Images | ❌ Avoid (lossy) |
| WAV | Audio | ✅ Perfect (uncompressed) |
| MP3 | Audio | ❌ Avoid (lossy) |
| MP4 | Video | ✅ Recommended |
| AVI | Video | ✅ Supported |

---

## Capacity Quick Reference

| Media Type | Formula | Example |
|------------|---------|---------|
| Image | `(W × H × 3) / 8` bytes | 800×600 = ~180 KB |
| Audio | `(samples) / 8` bytes | 3s@44kHz = ~16 KB |
| Video | `frames + audio` bytes | Varies greatly |

**Rule of Thumb:**
- 1 megapixel image ≈ 375 KB capacity
- 1 minute WAV audio ≈ 330 KB capacity

---

## Testing & Examples

```bash
# Run tests
python tests/test_image.py
python tests/test_audio.py
python tests/test_utils.py

# Run interactive examples
python examples.py
```

---

## Common Commands

### Check Capacity
```python
from modules import get_image_capacity, get_audio_capacity

capacity = get_image_capacity("image.png")
print(f"Can hide {capacity} bytes")
```

### With Encryption
```python
from utils.helpers import EncryptionHelper
from modules.image_steg import encode_image

enc = EncryptionHelper()
encrypted_msg = enc.encrypt_message("Secret", "password123")
encode_image("cover.png", encrypted_msg, "stego.png")
```

### Batch Processing
```python
import os
from modules.image_steg import encode_image

messages = ["Msg1", "Msg2", "Msg3"]
images = ["img1.png", "img2.png", "img3.png"]

for img, msg in zip(images, messages):
    encode_image(img, msg, f"stego_{img}")
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Import errors | Run `python verify_installation.py` |
| Video won't process | Install FFmpeg |
| Message too long | Use larger file or shorter message |
| Wrong key error | Use exact same key for decode |
| JPG corruption | Use PNG instead (lossless) |

---

## Security Tips

🔐 **Maximum Security Setup:**
1. ✅ Use encryption (AES-256)
2. ✅ Use key-based audio embedding
3. ✅ Use dual-channel video mode
4. ✅ Use strong passwords
5. ✅ Delete original cover files

⚠️ **What NOT to Do:**
- ❌ Use JPG for images (lossy)
- ❌ Forget encryption password
- ❌ Share stego-files publicly if sensitive
- ❌ Reuse same cover file multiple times

---

## Project Structure

```
STAGNOGRAPHY ANALIZER/
├── main_gui.py           # Launch this for GUI
├── examples.py           # Interactive examples
├── verify_installation.py # Check dependencies
├── modules/              # Core functionality
│   ├── image_steg.py
│   ├── audio_steg.py
│   └── video_steg.py
├── utils/                # Helper functions
│   └── helpers.py
├── tests/                # Test suite
└── docs/                 # Documentation
    ├── README.md
    ├── QUICKSTART.md
    └── ARCHITECTURE.md
```

---

## Key Shortcuts (GUI)

- **Alt+F4** - Exit application
- **Tab** - Switch between tabs
- **Ctrl+O** - Open file (when focused)
- **Ctrl+S** - Save file (when focused)

---

## Dependencies

```
Pillow          # Image processing
numpy           # Array operations
scipy           # Audio processing
opencv-python   # Video frames
moviepy         # Video/audio manipulation
pycryptodome    # AES encryption
```

---

## Support & Documentation

📖 **Full Documentation:** See `README.md`
🚀 **Quick Start:** See `QUICKSTART.md`
🏗️ **Architecture:** See `ARCHITECTURE.md`
📊 **Summary:** See `PROJECT_SUMMARY.md`

---

## Credits

**Project:** Steganography Analyzer
**Date:** November 27, 2025
**Status:** ✅ Production Ready
**License:** MIT

---

**Pro Tip:** Start with `python examples.py` to see everything in action! 🎉
