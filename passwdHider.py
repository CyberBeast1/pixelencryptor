from PIL import Image
from cryptography.fernet import Fernet
import os

def hide_text(image_path, text):
    try:
        image = Image.open(image_path).convert("RGB")
        binary_text = bytes_to_binary(text)
        binary_text += '00000000'  # Add a termination sequence (null character)
        
        pixels = image.load()
        index = 0
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = pixels[i, j]
                if index < len(binary_text):
                    r = (r & 0xFE) | int(binary_text[index])
                    index += 1
                if index < len(binary_text):
                    g = (g & 0xFE) | int(binary_text[index])
                    index += 1
                if index < len(binary_text):
                    b = (b & 0xFE) | int(binary_text[index])
                    index += 1
                pixels[i, j] = (r, g, b)
                if index >= len(binary_text):
                    break
        image.save('static/output_image.png')
        print("Text hidden successfully.")
    except Exception as e:
        print(f"An error occurred while hiding text: {e}")

def extract_text(image_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        binary_text = ""
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = pixels[i, j]
                binary_text += str(r & 1)
                binary_text += str(g & 1)
                binary_text += str(b & 1)
        
        text = ""
        for i in range(0, len(binary_text), 8):
            byte = binary_text[i:i+8]
            if byte == '00000000':  # Check for termination sequence
                break
            text += chr(int(byte, 2))
        return text
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return ""

def generate_key():
    key = Fernet.generate_key()
    with open("master.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists("master.key"):
        raise FileNotFoundError("Key file not found. Please generate a key first.")
    return open("master.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def bytes_to_binary(encrypted_message):
    binary_string = ''
    for byte in encrypted_message:
        binary_byte = format(byte, '08b')  # Convert byte to binary and pad with zeros
        binary_string += binary_byte
    return binary_string

if __name__ == '__main__':
    operation = input("Enter 'h' to hide text or 'e' to extract text or 'g' to generate key: ")
    if operation == 'h':
        message = input("Enter the text to hide: ")
        
        # Encrypt the message info
        encrypted = encrypt_message(message)
        print(f"Encrypted message: {encrypted}")
        print(f"Encrypted message length: {len(encrypted)}")
        with open('message.bin', 'wb') as f:
            f.write(encrypted)
            
        hide_text("image.png", encrypted)
        
    elif operation == 'e':
        hidden_text = extract_text('output_image.png')
        hidden_text = hidden_text.encode('utf-8')
        message = decrypt_message(hidden_text)
        
        print("Hidden message:", message)
        
    elif operation == 'g':
        key = generate_key()
        print(f"Generated key: {key}")
