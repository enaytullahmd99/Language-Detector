# 🚀 How to Run Language Detector App on Windows Server

## Quick Start (3 Steps)

### Step 1: Open PowerShell
Press `Win + X` and select "Windows PowerShell"

### Step 2: Navigate to App Directory
```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
```

### Step 3: Start the Server
```powershell
python app.py
```

**✅ Success! You should see:**
```
✅ Model and vectorizer loaded!

🚀 Starting Language Detector AI on port 5000
📍 Access the app at: http://127.0.0.1:5000
⚡ Press CTRL+C to stop the server
```

### Step 4: Open in Browser
Open any browser and go to: **http://127.0.0.1:5000**

---

## 📋 Prerequisites Check

Before running, ensure you have:

1. **Python 3.14.0** (already installed at your location)
2. **Required packages** (already installed)
3. **Model files** in the app directory:
   - `SVM_model.pkl`
   - `tfidf_vectorizer.pkl`

### Verify Installation
Run the diagnostic script:
```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
python diagnostic.py
```

You should see:
```
✅ ALL CHECKS PASSED!
🚀 Your app is ready to run!
```

---

## 🔧 Troubleshooting

### Issue 1: "Module not found" Error

**Solution:** Install required packages
```powershell
pip install Flask scikit-learn joblib pandas numpy regex gunicorn
```

Or use requirements.txt:
```powershell
pip install -r requirements.txt
```

### Issue 2: "Port 5000 already in use"

**Solution:** Kill the existing process
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace <PID> with actual number)
taskkill /PID <PID> /F
```

### Issue 3: "Model files not found"

**Solution:** Ensure you're in the correct directory
```powershell
# Check current directory
pwd

# Should show: C:\Users\enayt\Desktop\Enayat\Language Detector App

# List files
dir *.pkl
```

You should see:
- `SVM_model.pkl` (6.3 MB)
- `tfidf_vectorizer.pkl` (1.1 MB)

### Issue 4: Cannot connect to server in browser

**Possible causes:**
1. Server not running - Check terminal for "Running on..." message
2. Firewall blocking - Allow Python through Windows Firewall
3. Wrong URL - Use `http://127.0.0.1:5000` (not https)

**Solution:** Restart the server
```powershell
# Press CTRL+C to stop
# Then run again:
python app.py
```

---

## 🌐 Access from Other Devices

### On Same Network (Phone/Tablet/Other Computer)

1. **Find your computer's IP address:**
```powershell
ipconfig | findstr IPv4
```

Look for something like: `IPv4 Address. . . . . . . . . . . : 192.168.1.100`

2. **Start the server** (it automatically binds to 0.0.0.0)
```powershell
python app.py
```

3. **Access from other device:**
Open browser on your phone/tablet and go to:
```
http://192.168.1.100:5000
```
(Replace with your actual IP address)

---

## 📊 Testing the Application

### Test 1: Simple Browser Test
1. Open http://127.0.0.1:5000
2. Enter text: "Hello world"
3. Click "🔍 Detect Language"
4. Should show: "🇬🇧 English" in a popup

### Test 2: Multiple Languages
Try these:
- **French:** "Bonjour, comment allez-vous?"
- **Spanish:** "Hola, ¿cómo estás?"
- **German:** "Guten Tag, wie geht es Ihnen?"
- **Italian:** "Ciao, come stai?"
- **Hindi:** "नमस्ते, आप कैसे हैं?"
- **Malayalam:** "ഹലോ, സുഖമാണോ?"

### Test 3: API Test (PowerShell)
```powershell
$body = @{text='Bonjour le monde'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/predict' -Method POST -Body $body -ContentType 'application/json'
```

Expected output:
```
prediction
----------
French
```

### Test 4: History Feature
1. Detect several languages
2. Check the "📜 History" sidebar
3. Should show last 10 predictions
4. Click "Clear All" to reset

### Test 5: Statistics
After detecting multiple languages, check the stats cards:
- **⚡ Total Predictions** - Should increment
- **🎯 Most Detected** - Shows most common language
- **🌐 Unique Languages** - Counts different languages

---

## 🛑 Stopping the Server

Press `CTRL + C` in the PowerShell terminal

You should see:
```
^C
PS C:\Users\enayt\Desktop\Enayat\Language Detector App>
```

---

## 🔄 Restarting the Server

If you make any changes to the code:

1. Stop the server: `CTRL + C`
2. Start again: `python app.py`

---

## 📁 File Structure

Your app directory should have:

```
Language Detector App/
├── app.py                          # Main Flask application
├── SVM_model.pkl                   # Trained ML model (6.3 MB)
├── tfidf_vectorizer.pkl            # Text vectorizer (1.1 MB)
├── requirements.txt                # Python dependencies
├── diagnostic.py                   # System check script
├── Procfile                        # Deployment config
├── README.md                       # Project documentation
└── templates/
    └── index.html                  # Web interface
```

---

## 🎯 Features to Explore

### 1. **Text Input**
- Type or paste text in any supported language
- Press `Ctrl + Enter` for quick detection

### 2. **Modal Popups**
- Success: Green popup with detected language
- Warning: Yellow popup for empty input
- Error: Red popup for server errors

### 3. **Auto-Clear Input**
After successful detection, input clears automatically

### 4. **History Tracking**
- Sidebar shows last 10 predictions
- Includes timestamp for each
- Click "Clear All" to reset

### 5. **Statistics Dashboard**
- Total predictions count
- Most detected language
- Unique languages detected

### 6. **Supported Languages Section**
Scroll down to see all 17 supported languages with flags

### 7. **Responsive Design**
- Works on desktop, tablet, and mobile
- Purple gradient theme
- Glass-morphism effects

---

## 🌍 Supported Languages

The app can detect these 17 languages:

1. 🇬🇧 English
2. 🇮🇳 Malayalam
3. 🇮🇳 Hindi
4. 🇮🇳 Tamil
5. 🇮🇳 Kannada
6. 🇫🇷 French
7. 🇪🇸 Spanish
8. 🇵🇹 Portuguese
9. 🇮🇹 Italian
10. 🇷🇺 Russian
11. 🇸🇪 Swedish
12. 🇳🇱 Dutch
13. 🇸🇦 Arabic
14. 🇹🇷 Turkish
15. 🇩🇪 German
16. 🇩🇰 Danish
17. 🇬🇷 Greek

---

## 🚨 Common Issues & Fixes

### "Connection Error" in Browser

**Symptom:** Cannot connect popup appears  
**Cause:** Server stopped or not started  
**Fix:**
```powershell
# Check if server is running
netstat -ano | findstr :5000

# If nothing shows, start the server
python app.py
```

### "Server Error" Popup

**Symptom:** Red error popup when detecting  
**Cause:** Model loading issue or invalid input  
**Fix:**
```powershell
# Check server logs in terminal
# Look for error messages
# Restart server if needed
```

### Corrupted Emojis/Flags

**Symptom:** Boxes or ?? instead of flag emojis  
**Cause:** Browser encoding issue (already fixed in latest version)  
**Status:** ✅ Fixed in templates/index.html

---

## 📞 Quick Reference Commands

### Start Server
```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
python app.py
```

### Check Server Status
```powershell
netstat -ano | findstr :5000
tasklist /FI "IMAGENAME eq python.exe"
```

### Stop Server
Press `CTRL + C` in terminal

### Run Diagnostics
```powershell
python diagnostic.py
```

### Test API
```powershell
python test_api.py
```

### Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 💡 Pro Tips

1. **Keep terminal open** while using the app
2. **Use Ctrl + Enter** in text input for quick detection
3. **Test with different languages** to see history build up
4. **Check statistics** after multiple predictions
5. **Access from phone** using your computer's IP address
6. **Clear history** before showing to others for demo

---

## ✅ Success Checklist

Before calling it working, verify:

- [x] Terminal shows "✅ Model and vectorizer loaded!"
- [x] Terminal shows "Running on http://127.0.0.1:5000"
- [x] Browser opens at http://127.0.0.1:5000
- [x] Purple gradient background visible
- [x] Can type text in input box
- [x] "🔍 Detect Language" button works
- [x] Success popup appears with correct language
- [x] History sidebar updates
- [x] Statistics increment
- [x] All 17 languages show with correct flags
- [x] Footer shows "Md Enaytullah"

---

## 🎉 You're All Set!

Your Language Detector AI is now running successfully!

**Local Access:** http://127.0.0.1:5000  
**Network Access:** http://[YOUR-IP]:5000  
**Developer:** Md Enaytullah  
**Date:** October 22, 2025

---

## 📚 Additional Documentation

- `README.md` - Project overview
- `QUICK_START.md` - 3-step quick guide
- `STATUS_CHECK.md` - System status report
- `DEPLOYMENT_GUIDE.md` - Cloud deployment steps
- `HOW_TO_RUN.md` - Detailed setup guide

---

**Need help?** Run `python diagnostic.py` for automated system check!
