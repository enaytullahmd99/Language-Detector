# File: app.py
import os
import joblib
import regex as re
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Enable CORS and better error handling
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

# Store prediction history in memory
prediction_history = []

# --- LOAD MODEL AND VECTORIZER ---
try:
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('SVM_model.pkl')
    print("✅ Model and vectorizer loaded!")
except FileNotFoundError:
    print("❌ ERROR: Model/vectorizer files not found. Please run train_model.py first.")
    exit()

# --- HELPER FUNCTION ---
def clean_input(text):
    if not isinstance(text, str): return ""
    text = re.sub(r"[^\p{L}\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if request has JSON data
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        user_text = request.json.get('text')
        if not user_text:
            return jsonify({'error': 'No text provided'}), 400

        if not user_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400

        cleaned_text = clean_input(user_text)
        
        if not cleaned_text:
            return jsonify({'error': 'Text contains no valid characters'}), 400
        
        input_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(input_vector)[0]
        
        # Add to history
        history_entry = {
            'text': user_text,
            'prediction': prediction,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        prediction_history.insert(0, history_entry)  # Add to beginning
        
        # Keep only last 10 predictions
        if len(prediction_history) > 10:
            prediction_history.pop()
        
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({'error': 'Server error occurred. Please try again.'}), 500

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify({'history': prediction_history})

@app.route('/clear-history', methods=['POST'])
def clear_history():
    prediction_history.clear()
    return jsonify({'message': 'History cleared'})

# --- RUN APP ---
if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    print(f"\n🚀 Starting Language Detector AI on port {port}")
    print(f"📍 Access the app at: http://127.0.0.1:{port}")
    print(f"⚡ Press CTRL+C to stop the server\n")
    # Run on all interfaces (0.0.0.0) for deployment
    app.run(debug=False, host='0.0.0.0', port=port)