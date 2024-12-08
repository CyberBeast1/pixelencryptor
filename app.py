from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
from passwdHider import hide_text, extract_text, generate_key, encrypt_message, decrypt_message, load_key

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide', methods=['POST'])
def hide():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    message = request.form['message']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Encrypt the message
        encrypted = encrypt_message(message)

        # Hide the encrypted message in the image
        hide_text(file_path, encrypted)
        
        # key used
        key = load_key()
        
        return render_template('result.html', result=f'<h3><strong style=\'color:white;\'>Encrypted Message: </strong>{encrypted}</h3><br><h4><strong style=\'color:white;\'>Key Used: </strong>{key}</h4>', image_path='output_image.png')

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Extract the hidden text
        hidden_text = extract_text(file_path)
        hidden_text = hidden_text.encode('utf-8')
        
        # Decrypt the hidden message
        message = decrypt_message(hidden_text)
        
        return render_template('result.html', result=f'<h2><strong style=\'color:white;\'>Hidden message: </strong>{message}</h2>')

if __name__ == '__main__':
    app.run(debug=True)