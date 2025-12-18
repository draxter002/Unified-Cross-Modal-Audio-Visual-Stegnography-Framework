# 📖 How to Use the Steganography Framework

## What is Steganography?

Steganography is the practice of hiding secret messages inside ordinary files (like images or audio) so that only people who know the secret can find and read the message. Unlike encryption, which scrambles the message, steganography hides it completely!

---

## 🖼️ Hiding Messages in Images

### Encode (Hide a Message)

1. **Select "Image Steganography" tab** at the top
2. **Click "Select Cover Image"** and choose a PNG or BMP image
   - The app will show you how much text you can hide
3. **Type your secret message** in the text box
4. **(Optional) Enable encryption:**
   - Check "Encrypt message"
   - Enter a password
   - This adds extra security!
5. **Click "Encode Message"**
6. **Download your stego-image**
   - This image looks identical to the original
   - But contains your hidden message!

### Decode (Extract a Message)

1. **Select "Image Steganography" tab**
2. **Click "Decode Message" button** (top of the form)
3. **Upload the stego-image** (the image with hidden message)
4. **(If encrypted) Check "Message is encrypted"** and enter password
5. **Click "Decode Message"**
6. **Your secret message appears!**

---

## 🎵 Hiding Messages in Audio

### Encode (Hide a Message)

1. **Select "Audio Steganography" tab** at the top
2. **Click "Select Cover Audio"** and choose a WAV file
   - The app shows capacity (how much you can hide)
3. **Type your secret message**
4. **(Optional) Enable encryption** with password
5. **(Optional) Enter a steganography key**
   - This makes the message harder to detect
   - Remember this key - you'll need it to decode!
6. **Click "Encode Message"**
7. **Download your stego-audio**
   - Sounds identical to original
   - Contains hidden message!

### Decode (Extract a Message)

1. **Select "Audio Steganography" tab**
2. **Click "Decode Message"** button
3. **Upload the stego-audio** file
4. **(If encrypted)** Check "Message is encrypted" and enter password
5. **(If you used a key)** Enter the steganography key
6. **Click "Decode Message"**
7. **Your secret message appears!**

---

## 🔐 Security Tips

### Basic Hiding (No Encryption)
- **Who can read it?** Anyone who knows about steganography
- **Use when:** Sharing with friends, low security needs
- **Pros:** Simple, no password needed
- **Cons:** Message is not encrypted

### With Encryption
- **Who can read it?** Only people with the password
- **Use when:** Sensitive information, high security
- **Pros:** Message is encrypted AND hidden
- **Cons:** Must remember password (can't recover if lost!)

### With Steganography Key (Audio Only)
- **What it does:** Hides message in random positions
- **Use when:** Extra stealth needed
- **Pros:** Harder to detect
- **Cons:** Must remember key

### Best Security: All Three!
1. Encrypt with password ✓
2. Use steganography key (audio) ✓
3. Hide in file ✓

Result: Your message is encrypted, hidden, and scattered!

---

## 💡 Tips & Tricks

### File Selection
- **Images:** PNG and BMP work best (lossless formats)
  - ❌ Don't use JPEG (compression destroys hidden data)
- **Audio:** WAV files only
  - ❌ Don't use MP3 (compression ruins hidden data)

### Capacity
- **Bigger files = more space**
- 1920×1080 image ≈ 777 KB of text
- 1-minute WAV audio ≈ varies by quality
- Check capacity before encoding!

### Message Length
- Keep messages under capacity limit
- The app will tell you if message is too long
- Compress long texts or use bigger files

### Password Safety
- **Use strong passwords** (mix letters, numbers, symbols)
- **Write it down** somewhere safe
- **Lost password = lost message** (no recovery!)

### Steganography Keys
- Can be any text: "mySecret123", "pizza", etc.
- Must use EXACT same key to decode
- Case-sensitive: "Secret" ≠ "secret"

---

## 🎯 Use Cases

### Personal
- **Secret notes to friends**
- **Hide passwords in innocent-looking images**
- **Store sensitive info in plain sight**
- **Digital watermarking**

### Professional
- **Secure communications**
- **Copyright protection**
- **Data integrity verification**
- **Covert channels**

### Education
- **Learn about security**
- **Understand LSB technique**
- **Experiment with cryptography**

---

## ⚠️ Important Notes

### Don't Modify Stego Files!
- **❌ Don't edit the image/audio**
- ❌ Don't compress or convert format
- ❌ Don't crop, resize, or filter
- ✓ Keep the exact file as-is

### If Decoding Fails
1. **Check you're using the right file**
2. **Verify password is correct** (if encrypted)
3. **Confirm steganography key** (if used for audio)
4. **Ensure file wasn't modified**
5. **Check file format** (PNG/BMP for images, WAV for audio)

### Privacy
- **Your files are processed locally** (if running locally)
- **Files are deleted** after processing
- **No data is stored** permanently
- **Use HTTPS** when accessing online

---

## 📱 Works On All Devices

- **Desktop:** Windows, Mac, Linux
- **Mobile:** iPhone, Android (via web browser)
- **Tablet:** iPad, Android tablets

Just visit the website in any modern browser!

---

## 🆘 Troubleshooting

### "Message too long" Error
- **Solution:** Use a larger cover file or shorter message

### "Decryption failed" Error
- **Solution:** Check password is correct (case-sensitive!)

### "Error decoding audio" with Key
- **Solution:** Enter exact key used during encoding

### Upload Button Doesn't Work
- **Solution:** Check file format (PNG/BMP for images, WAV for audio)

### Decoded Message is Gibberish
- **Possible causes:**
  1. Wrong password
  2. Wrong steganography key
  3. File was modified after encoding
  4. Trying to decode a normal file (no hidden message)

---

## 🎓 How It Works (Technical)

### LSB (Least Significant Bit) Technique

1. **Images:**
   - Each pixel has Red, Green, Blue values (0-255)
   - We modify the last bit of each color
   - Example: 156 (10011100) → 157 (10011101)
   - Change is invisible to human eye!

2. **Audio:**
   - Each audio sample is a number
   - We modify the last bit
   - Change is inaudible!

3. **Message Storage:**
   - Text → Binary (0s and 1s)
   - Each bit replaces LSB in file
   - Special delimiter marks end: `<<<END>>>`

4. **Encryption (Optional):**
   - AES-256 encryption
   - Password → SHA-256 → Encryption key
   - Message encrypted before hiding

---

## 🎉 Have Fun!

Steganography is powerful and fun. Use it responsibly and ethically!

**Remember:** With great hiding power comes great responsibility. 😊

---

## 📞 Support

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for technical setup
- Read [START_HERE.md](START_HERE.md) for deployment guide
- Visit `/docs` endpoint for API documentation

**Happy hiding! 🔒**
