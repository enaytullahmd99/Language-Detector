Render deployment - step-by-step

This document walks you through deploying your Language Detector App to Render.com.

Prerequisites
- A Render account (https://render.com). Create one if you don't have it.
- A GitHub account and a repository to push your project to.
- Your project folder contains: `app.py`, `templates/`, `SVM_model.pkl`, `tfidf_vectorizer.pkl`, `requirements.txt`, `Procfile`.

1) Prepare repo locally

Open PowerShell in your project root:

```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
```

If you haven't initialized git yet:

```powershell
git init
git add .
git commit -m "Initial commit - Language Detector App"
```

If you already have a repo, just add/commit new files:

```powershell
git add .
git commit -m "Prepare for Render deployment: add Procfile and gunicorn"
```

Push to GitHub (create a repo on GitHub first, then):

```powershell
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

Notes about model files
- If `SVM_model.pkl` and `tfidf_vectorizer.pkl` are large (>50MB) consider using Git LFS or store them in an object store (S3) and download at startup.
- To use Git LFS:

```powershell
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git add *.pkl
git commit -m "Add model files via LFS"
git push origin main
```

2) Create a new Web Service on Render

- Sign in to Render.
- Click "New+" → "Web Service".
- Connect your GitHub repo and pick the repository you pushed.
- Fill deployment settings:
  - Environment: **Python 3**
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn --workers 3 --bind 0.0.0.0:$PORT app:app` (Procfile is respected too)
  - Branch: `main`
  - Name: choose a friendly name
- Click **Create Web Service**.

3) Wait for Build & Deploy
- Render will install dependencies and run your app.
- Watch logs on the Render web UI; if install fails, check `requirements.txt` and Python version.

4) Post-deploy checks
- Visit the assigned URL (e.g. https://your-app.onrender.com)
- Test the home page and run a prediction via the UI
- If model loading fails, check logs for missing files or memory issues

5) Debugging tips
- If you used Git LFS and model files are missing, confirm LFS files stored properly and Render supports LFS (they do).
- If memory is insufficient, consider moving model to an object store and download at start, or use smaller model.
- Add environment variables in Render dashboard if needed (e.g., model path, SECRET keys).

6) Security & performance
- Use HTTPS (Render provides it by default)
- Consider adding basic auth or rate limiting if public
- Use a proper WSGI server (gunicorn already used)
- For larger scale, use a persistent database for history instead of in-memory list

That's it — your app should now be live on Render!
