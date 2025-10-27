@echo off
REM Language Detector App - Start Script (Batch Version)

echo.
echo ========================================
echo   Language Detector AI - Starting
echo ========================================
echo.

REM Check if app.py exists
if not exist "app.py" (
    echo [ERROR] app.py not found!
    echo Please run this script from the app directory.
    echo.
    pause
    exit /b 1
)

REM Check if model files exist
if not exist "SVM_model.pkl" (
    echo [ERROR] SVM_model.pkl not found!
    echo Please ensure model files are in the directory.
    echo.
    pause
    exit /b 1
)

if not exist "tfidf_vectorizer.pkl" (
    echo [ERROR] tfidf_vectorizer.pkl not found!
    echo Please ensure model files are in the directory.
    echo.
    pause
    exit /b 1
)

echo [OK] All files present!
echo.
echo Starting Flask server...
echo.
echo Once started, open your browser to:
echo    http://127.0.0.1:5000
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.

REM Start the Flask app
python app.py
