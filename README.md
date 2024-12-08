# PixelEncryptor

PixelEncryptor is a Python-based steganography project that securely hides and extracts encrypted text messages within images. It combines image processing with encryption to ensure the confidentiality of hidden data.

---

## Features

- **Secure Encryption**: Uses `cryptography.fernet` for encrypting and decrypting messages.
- **Steganography**: Embeds encrypted messages into images at the pixel level without noticeable changes.
- **Flask Web Interface**: User-friendly interface for hiding and extracting messages.
- **Key Management**: Generates and securely stores encryption keys.
- **Cross-Compatibility**: Supports common image formats like `.png` and `.jpg`.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PixelEncryptor.git
   cd PixelEncryptor
   ```
2. Install dependencies:
    ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Access the web interface at `http://127.0.0.1:5000/`.

---

## Usage

### Via Command Line

1. Generate a Key:
    ```bash
    python passwdHider.py
    ```
    Select option `g` to generate and save a key.

2. Hide Text in an Image:
    - Place the image as image.png in the working directory.
    - Run the script and select option `h`.
    - Provide the message to hide.
    - The output will be saved as static/output_image.png.

3. Extract Hidden Text:
    - Ensure static/output_image.png exists.
    - Run the script and select option `e` to extract the message.

### Via Web Interface

1. Open the app in your browser.
2. Hide a Message:
    - Upload an image.
    - Enter the text message.
    - The app encrypts and hides the message in the image.
    - Download the output image.
3. Extract a Message:
    - Upload an image containing the hidden message.
    - The app decrypts and displays the message.

## Notes
> Ensure the encryption key is securely stored to avoid loss of hidden data.
> The message length is limited by the image size and pixel capacity.