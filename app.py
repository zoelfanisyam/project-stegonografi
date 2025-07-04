from flask import Flask, render_template, request, send_file, send_from_directory
import os
from stegano_alpha import embed_message, extract_message
import cv2
import werkzeug

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        operation = request.form.get('operation')
        image_file = request.files.get('image')
        pin = request.form.get('pin')

        if not image_file or not pin:
            return "Gambar dan PIN wajib diisi!", 400

        filename = werkzeug.utils.secure_filename(image_file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image_file.save(image_path)

        if operation == 'embed':
            message = request.form.get('message')
            if not message:
                return "Pesan tidak boleh kosong saat menyisipkan!", 400

            stego_image = embed_message(image_path, message, pin)

            base_filename = os.path.splitext(filename)[0]
            stego_filename = f'stego_{base_filename}.png'
            stego_path = os.path.join(OUTPUT_FOLDER, stego_filename)
            cv2.imwrite(stego_path, stego_image)

            return send_file(stego_path, as_attachment=True)

        elif operation == 'extract':
            extracted_msg, valid = extract_message(image_path, pin)
            if valid:
                return render_template('result.html',
                                       original=filename,
                                       stego=filename,
                                       message=extracted_msg)
            else:
                return "❌ PIN salah atau pesan tidak valid!", 403

        else:
            return "Operasi tidak dikenal.", 400

    return render_template('index.html')

# Untuk load gambar statis
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/outputs/<filename>')
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
