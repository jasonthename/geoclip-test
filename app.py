import os
from flask import Flask, request, render_template, jsonify
import torch
from geoclip import GeoCLIP
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize GeoCLIP model
model = GeoCLIP()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Get predictions from GeoCLIP
            top_pred_gps, top_pred_prob = model.predict(filepath, top_k=5)
            
            # Format predictions
            predictions = []
            for i in range(5):
                lat, lon = top_pred_gps[i]
                predictions.append({
                    'latitude': float(lat),
                    'longitude': float(lon),
                    'probability': float(top_pred_prob[i])
                })
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify({'predictions': predictions})
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)