# Installation & Setup Guide

## Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/enaytullahmd99/Language-Detector.git
cd Language-Detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- Flask==3.0.0
- scikit-learn==1.3.2
- joblib==1.3.2
- pandas==2.1.3
- numpy==1.26.2
- regex
- gunicorn==20.1.0

### 3. Verify Model Files
Make sure these files exist in the project directory:
- `SVM_model.pkl` - Trained SVM language detection model
- `tfidf_vectorizer.pkl` - TF-IDF vectorizer for text processing

### 4. Run the Application

**Local Development:**
```bash
python app.py
```

The app will start on `http://127.0.0.1:5000`

**Production (using Gunicorn):**
```bash
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
```

## Troubleshooting

### ModuleNotFoundError: No module named 'joblib'
**Solution:** Install all dependencies
```bash
pip install -r requirements.txt
```

### Model files not found
**Solution:** Ensure `SVM_model.pkl` and `tfidf_vectorizer.pkl` are in the project root directory.

### Port already in use
**Solution:** Use a different port
```bash
python app.py
# Or manually set PORT environment variable
```

## Docker Deployment (Optional)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:app"]
```

## Environment Variables
- `PORT` - Port number (default: 5000)

## Support
For issues, please check the GitHub repository or create an issue.
