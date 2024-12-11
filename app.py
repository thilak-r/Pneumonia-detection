from flask import Flask, request, render_template, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = load_model('pneumonia_detection_model.h5')

# Define class names
class_names = ['NORMAL', 'PNEUMONIA']

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the uploaded file
        filepath = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)

        # Load and preprocess the image
        img = image.load_img(filepath, target_size=(220, 220))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = class_names[int(np.round(prediction[0][0]))]

        # Remove the temporary file
        os.remove(filepath)

        return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
