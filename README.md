# 🌍 Language Detector AI

A beautiful, AI-powered web application that detects the language of any text using Machine Learning.

![Language Detector](https://img.shields.io/badge/Languages-20+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![ML](https://img.shields.io/badge/ML-SVM-orange)

## ✨ Features

- 🎯 **Accurate Detection** - Detects 15+ languages with high accuracy
- 🎨 **Beautiful UI** - Modern, responsive design with gradient backgrounds
- 📊 **Statistics Dashboard** - Track your predictions and most detected languages
- 📜 **History Tracking** - View your recent language detections
- 🔔 **Smart Popups** - Beautiful modal notifications for all actions
- 📱 **Mobile Friendly** - Works perfectly on all devices
- ⚡ **Fast & Real-time** - Instant predictions

## 🚀 Quick Start

### Local Development

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure you have the model files:**
   - `SVM_model.pkl`
   - `tfidf_vectorizer.pkl`
   
   If not, train the model first by running `train_model.py`

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   ```
   http://localhost:5000
   ```

## 🌐 Deployment

See **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** for detailed instructions on deploying to:
- Render (Recommended)
- PythonAnywhere
- Railway
- Vercel
- Heroku

## 🛠️ Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **ML Model:** Support Vector Machine (SVM)
- **Vectorization:** TF-IDF
- **Libraries:** scikit-learn, joblib, pandas

## 📁 Project Structure

```
Language Detector App/
├── app.py                      # Flask backend
├── templates/
│   └── index.html             # Frontend UI
├── SVM_model.pkl              # Trained ML model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── train_model.py             # Model training script
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment configuration
├── DEPLOYMENT_GUIDE.md        # Deployment instructions
└── README.md                  # This file
```

## 🎯 Supported Languages

English, Spanish, French, German, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, Hindi, Turkish, Polish, Swedish, Danish, Norwegian, Finnish, Greek, and more!

## 💡 How It Works

1. User enters text in any language
2. Text is cleaned and preprocessed
3. TF-IDF vectorization is applied
4. SVM model predicts the language
5. Result is displayed in a beautiful popup
6. History is automatically tracked

## 🔧 Customization

- **Change theme colors:** Edit the gradient in `index.html` (line 10)
- **Add more languages:** Retrain the model with additional data
- **Modify UI:** Update Tailwind classes in `index.html`

## 📝 Updates in Latest Version

- ✅ Auto-clear input after prediction
- ✅ Beautiful modal popups for all notifications
- ✅ Warning popup for empty input
- ✅ Success popup with detected language
- ✅ Error handling with user-friendly messages
- ✅ Deployment-ready configuration

## 🤝 Contributing

Feel free to fork this project and make improvements!

## 📄 License

Free to use for personal and educational purposes.

## 👨‍💻 Author

Created with ❤️ by Enayat

---

**Happy Language Detecting! 🌍✨**
