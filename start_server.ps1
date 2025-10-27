# Language Detector App - Start Script
# This script starts the Flask server automatically

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🌍 Language Detector AI - Starting   " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the right directory
if (-Not (Test-Path "app.py")) {
    Write-Host "❌ Error: app.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the app directory." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Current directory: $PWD" -ForegroundColor Yellow
    Write-Host "Expected directory: c:\Users\enayt\Desktop\Enayat\Language Detector App" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

# Check if model files exist
if (-Not (Test-Path "SVM_model.pkl")) {
    Write-Host "❌ Error: SVM_model.pkl not found!" -ForegroundColor Red
    Write-Host "Please ensure model files are in the directory." -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

if (-Not (Test-Path "tfidf_vectorizer.pkl")) {
    Write-Host "❌ Error: tfidf_vectorizer.pkl not found!" -ForegroundColor Red
    Write-Host "Please ensure model files are in the directory." -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host "✅ All files present!" -ForegroundColor Green
Write-Host ""

# Check if port 5000 is already in use
$portInUse = netstat -ano | findstr :5000
if ($portInUse) {
    Write-Host "⚠️  Warning: Port 5000 is already in use!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Do you want to kill the existing process? (Y/N)" -ForegroundColor Yellow
    $response = Read-Host
    
    if ($response -eq "Y" -or $response -eq "y") {
        $pid = ($portInUse -split '\s+')[-1]
        Write-Host "Killing process $pid..." -ForegroundColor Yellow
        taskkill /PID $pid /F
        Start-Sleep -Seconds 2
    } else {
        Write-Host "Exiting..." -ForegroundColor Red
        pause
        exit 1
    }
}

Write-Host "🚀 Starting Flask server..." -ForegroundColor Cyan
Write-Host ""
Write-Host "📍 Once started, open your browser to:" -ForegroundColor Green
Write-Host "   http://127.0.0.1:5000" -ForegroundColor White
Write-Host ""
Write-Host "⚡ Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start the Flask app
python app.py
