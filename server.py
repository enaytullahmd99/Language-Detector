from flask import Flask, request, jsonify, send_from_directory
import joblib
import os
import regex as re

app = Flask(__name__)

# Load model and vectorizer (update the model name if needed)
MODEL_PATH = "SVM_model.pkl"  # Change if your best model is different
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError("Model or vectorizer file not found. Please train and save them first.")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def clean_input(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^\p{L}\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.route("/", methods=["GET"])
def index():
    return send_from_directory('.', 'index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    cleaned = clean_input(text)
    X_input = vectorizer.transform([cleaned])
    prediction = model.predict(X_input)[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
