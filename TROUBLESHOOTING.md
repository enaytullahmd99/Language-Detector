# Troubleshooting Guide

## Common Issues and Solutions

### 1. ModuleNotFoundError: No module named 'joblib' (or Flask, scikit-learn, etc.)

**Error:**
```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    import joblib
ModuleNotFoundError: No module named 'joblib'
```

**Solution:**
```bash
pip install -r requirements.txt
```

If that doesn't work, install packages individually:
```bash
pip install Flask scikit-learn joblib pandas numpy regex gunicorn
```

**Root Cause:** Dependencies not installed in your current Python environment.

---

### 2. Model/Vectorizer Files Not Found

**Error:**
```
❌ ERROR: Model/vectorizer files not found. Please run train_model.py first.
```

**Solution:**
1. Check if these files exist in your project folder:
   - `SVM_model.pkl`
   - `tfidf_vectorizer.pkl`

2. If missing, train the model:
```bash
python train_model.py
```

3. Ensure the files are in the same directory as `app.py`

---

### 3. Port Already in Use

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**

**Windows:**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
# Find and kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

Or use a different port:
```bash
# Set PORT environment variable
export PORT=8000  # Linux/Mac
$env:PORT=8000    # Windows PowerShell

python app.py
```

---

### 4. scikit-learn Build Error on Windows

**Error:**
```
Microsoft Visual C++ 14.0 or greater is required
```

**Solution:**

**Option 1: Install Build Tools**
1. Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Install "Desktop development with C++"
3. Restart terminal and reinstall:
   ```bash
   pip install scikit-learn
   ```

**Option 2: Use Conda (Easier)**
```bash
conda create -n langdetect python=3.10
conda activate langdetect
pip install -r requirements.txt
```

**Option 3: Use Pre-built Wheels**
```bash
pip install --upgrade pip
pip install scikit-learn
```

---

### 5. Version Compatibility Issues

**Error:**
```
ImportError: cannot import name 'X' from 'sklearn'
```

**Solution:**
Use compatible versions specified in `requirements.txt`:
```bash
pip install Flask==3.0.0 scikit-learn==1.3.2 joblib==1.3.2 pandas==2.1.3 numpy==1.26.2
```

If using Python 3.14 or newer, you may need newer package versions:
```bash
pip install --upgrade Flask scikit-learn joblib pandas numpy
```

---

### 6. CORS Errors in Browser

**Error:**
```
Access to fetch at 'http://127.0.0.1:5000/predict' blocked by CORS policy
```

**Solution:**
The app already includes CORS headers. If still having issues:

1. Check `app.py` has:
```python
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response
```

2. Or install Flask-CORS:
```bash
pip install flask-cors
```

Add to `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

### 7. Empty Predictions or Server Errors

**Error:**
Server returns 500 error or empty responses.

**Solution:**

1. Check server logs for specific error
2. Verify input text is not empty
3. Ensure model can handle the input:
```python
# Test model manually
import joblib
model = joblib.load('SVM_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

text = "Hello world"
vec = vectorizer.transform([text])
print(model.predict(vec))
```

---

### 8. Gunicorn Not Working on Windows

**Error:**
```
ModuleNotFoundError: No module named 'fcntl'
```

**Solution:**
Gunicorn doesn't work natively on Windows. Use for deployment (Linux/Render) only.

For local Windows development:
```bash
python app.py
```

For Windows production, use Waitress:
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

---

### 9. Git Push Rejected

**Error:**
```
! [rejected] main -> main (fetch first)
```

**Solution:**
```bash
git pull origin main --allow-unrelated-histories
# Resolve any conflicts
git add .
git commit -m "Resolve merge conflicts"
git push origin main
```

---

### 10. Render Deployment Fails

**Common Issues:**

**Build fails:**
- Check `requirements.txt` is in root
- Ensure Python version compatibility
- Check build logs for specific error

**App crashes after deploy:**
- Verify `Procfile` exists:
  ```
  web: gunicorn --workers 3 --bind 0.0.0.0:$PORT app:app
  ```
- Check model files are committed to Git
- Review Render logs for errors

**Model files too large:**
- Use Git LFS:
  ```bash
  git lfs install
  git lfs track "*.pkl"
  git add .gitattributes
  git add *.pkl
  git commit -m "Add model files via LFS"
  git push origin main
  ```

---

## Still Having Issues?

1. **Check Python version:**
   ```bash
   python --version
   ```
   Recommended: Python 3.10 - 3.12

2. **Create a fresh virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\Activate   # Windows
   pip install -r requirements.txt
   ```

3. **Check all files are present:**
   ```
   ✓ app.py
   ✓ requirements.txt
   ✓ Procfile
   ✓ SVM_model.pkl
   ✓ tfidf_vectorizer.pkl
   ✓ templates/index.html
   ```

4. **Clear pip cache:**
   ```bash
   pip cache purge
   pip install --no-cache-dir -r requirements.txt
   ```

## Need More Help?

- Check the GitHub Issues: https://github.com/enaytullahmd99/Language-Detector/issues
- Review deployment guides in `DEPLOYMENT_GUIDE.md`
- Check installation steps in `INSTALLATION_GUIDE.md`
