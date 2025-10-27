# 🚀 How to Run Your Language Detector Application

## ✅ COMPLETE STEP-BY-STEP GUIDE

---

## 📋 Pre-Requirements Check

Before running the application, ensure you have:

### 1. Python Installed
- ✅ Python 3.8 or higher
- Check: `python --version`

### 2. Required Files Present
All these files should be in your `Language Detector App` folder:
- ✅ `app.py` - Main Flask application
- ✅ `templates/index.html` - Frontend HTML
- ✅ `SVM_model.pkl` - Trained ML model
- ✅ `tfidf_vectorizer.pkl` - Text vectorizer
- ✅ `requirements.txt` - Python dependencies

---

## 🔧 STEP 1: Install Required Packages

Open PowerShell or Command Prompt and navigate to your app folder:

```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
```

Install all required Python packages:

```powershell
pip install Flask joblib regex scikit-learn pandas numpy
```

**Or install from requirements.txt:**

```powershell
pip install -r requirements.txt
```

---

## 🚀 STEP 2: Start the Flask Server

### Method 1: Using Python Command (Recommended)

```powershell
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"
python app.py
```

### Method 2: Using Python with Full Path

```powershell
python "c:\Users\enayt\Desktop\Enayat\Language Detector App\app.py"
```

### ✅ Expected Output:

```
✅ Model and vectorizer loaded!
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.27.34.64:5000
Press CTRL+C to quit
```

**⚠️ IMPORTANT:** Leave this terminal window open while using the app!

---

## 🌐 STEP 3: Open the Application in Your Browser

Once the server is running, open any web browser and go to:

```
http://127.0.0.1:5000
```

**Alternative URLs (all work the same):**
- http://localhost:5000
- http://10.27.34.64:5000 (accessible from other devices on your network)

---

## 🧪 STEP 4: Test the Application

### Frontend Testing:

1. **Enter Text:** Type or paste any text in the textarea
   - Example: "Hello, how are you?"
   - Example: "Bonjour, comment allez-vous?"
   - Example: "Hola, ¿cómo estás?"

2. **Click "Detect Language"** button

3. **Expected Result:**
   - ✅ Success popup appears
   - ✅ Language is displayed
   - ✅ Input box clears automatically
   - ✅ History is updated
   - ✅ Statistics update

### Backend Testing (Optional):

Test the API endpoint directly using PowerShell:

```powershell
$body = @{text='Hello world'} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -ContentType "application/json" -Body $body
```

**Expected Response:**
```json
{"prediction":"English"}
```

---

## 🛑 STEP 5: Stop the Server

When you're done:

1. Go to the terminal where the server is running
2. Press `CTRL + C`
3. The server will stop

---

## ⚠️ COMMON ISSUES & SOLUTIONS

### Issue 1: "Connection Error" in Browser

**Problem:** Frontend shows "Connection Error! Please check your connection and try again."

**Solution:**
1. Check if the server is running (terminal should show "Running on...")
2. If not running, restart it: `python app.py`
3. Refresh the browser page

---

### Issue 2: "Model/vectorizer files not found"

**Problem:** Terminal shows "❌ ERROR: Model/vectorizer files not found"

**Solution:**
1. Make sure these files exist in the same folder as `app.py`:
   - `SVM_model.pkl`
   - `tfidf_vectorizer.pkl`
2. If missing, run the training script:
   ```powershell
   python train_model.py
   ```

---

### Issue 3: "ModuleNotFoundError: No module named..."

**Problem:** Terminal shows "ModuleNotFoundError: No module named 'Flask'" (or similar)

**Solution:**
Install the missing package:
```powershell
pip install Flask joblib regex scikit-learn pandas
```

---

### Issue 4: Port Already in Use

**Problem:** Terminal shows "Address already in use" or "Port 5000 is already in use"

**Solution:**

**Option A:** Stop other apps using port 5000

**Option B:** Change the port in `app.py`:
```python
port = int(os.environ.get('PORT', 5001))  # Change 5000 to 5001
```
Then access: http://127.0.0.1:5001

---

### Issue 5: Browser Shows "Cannot GET /"

**Problem:** Blank page or "Cannot GET /"

**Solution:**
1. Make sure the `templates` folder exists
2. Make sure `index.html` is inside the `templates` folder
3. Restart the server

---

## 📱 ACCESSING FROM OTHER DEVICES

To access your app from a phone or another computer on the same network:

1. Find your computer's IP address:
   ```powershell
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. On the other device, open browser and go to:
   ```
   http://YOUR_IP:5000
   ```
   Example: http://192.168.1.100:5000

**Note:** Your computer's firewall must allow connections on port 5000

---

## 🔄 QUICK START COMMANDS

### Full Start Sequence:

```powershell
# 1. Navigate to folder
cd "c:\Users\enayt\Desktop\Enayat\Language Detector App"

# 2. Install packages (first time only)
pip install -r requirements.txt

# 3. Start server
python app.py

# 4. Open browser to http://127.0.0.1:5000
```

### Stop Server:
```
Press CTRL + C in the terminal
```

---

## 📊 FEATURES TO TEST

Once your app is running, test these features:

### ✅ Main Features:
1. **Language Detection** - Enter text and click detect
2. **Modal Popups** - Success, warning, and error popups
3. **Auto-clear Input** - Input clears after prediction
4. **History Tracking** - View recent predictions in sidebar
5. **Statistics** - Total predictions, most detected, unique languages
6. **Supported Languages** - Scroll down to see all 17 languages
7. **Clear History** - Click "Clear All" in history section
8. **Keyboard Shortcut** - Press Ctrl+Enter to detect

### ✅ Test Different Languages:
- English: "Hello, how are you?"
- French: "Bonjour, comment allez-vous?"
- Spanish: "Hola, ¿cómo estás?"
- German: "Guten Tag, wie geht es Ihnen?"
- Italian: "Ciao, come stai?"
- Portuguese: "Olá, como você está?"

---

## 🎯 EXPECTED BEHAVIOR

### When App is Working Correctly:

1. **Server Starts:**
   - Terminal shows "✅ Model and vectorizer loaded!"
   - No error messages
   - Shows "Running on http://127.0.0.1:5000"

2. **Browser Opens:**
   - Beautiful purple gradient background
   - "Language Detector AI" header
   - Text input box
   - History sidebar on the right
   - Statistics cards below
   - Supported languages section
   - Footer with copyright

3. **Language Detection:**
   - Type text → Click button → Popup shows → Result appears → Input clears
   - History updates automatically
   - Statistics update in real-time

---

## 🐛 DEBUGGING TIPS

### Check Server Status:
1. Look at the terminal where you ran `python app.py`
2. Should show: "Running on http://127.0.0.1:5000"
3. No error messages should appear

### Check Browser Console:
1. Press `F12` in your browser
2. Go to "Console" tab
3. Look for any red error messages
4. Common issue: "Failed to fetch" means server isn't running

### Check Network Tab:
1. Press `F12` in your browser
2. Go to "Network" tab
3. Click "Detect Language"
4. Look for `/predict` request
5. Should show status "200 OK"

---

## 📝 FILE STRUCTURE VERIFICATION

Your folder should look like this:

```
Language Detector App/
├── app.py                      ← Main Flask server
├── templates/
│   └── index.html             ← Frontend UI
├── SVM_model.pkl              ← Trained model
├── tfidf_vectorizer.pkl       ← Vectorizer
├── requirements.txt           ← Dependencies
├── train_model.py             ← Model training script
├── languagedetection.csv      ← Training data
└── README.md                  ← Documentation
```

---

## ✅ SUCCESS CHECKLIST

Before reporting issues, verify:

- [ ] Python 3.8+ is installed
- [ ] All packages are installed (`pip install -r requirements.txt`)
- [ ] Model files exist (SVM_model.pkl, tfidf_vectorizer.pkl)
- [ ] templates/index.html exists
- [ ] Server starts without errors
- [ ] Terminal shows "Running on http://127.0.0.1:5000"
- [ ] Browser can access http://127.0.0.1:5000
- [ ] No firewall blocking port 5000

---

## 🎉 YOUR APP IS READY!

If you see the beautiful purple gradient interface with:
- Language Detector AI header ✅
- Text input box ✅
- History sidebar ✅
- Statistics cards ✅
- 17 supported languages listed ✅
- Footer with "Md Enaytullah" ✅

**Congratulations! Your app is working perfectly!** 🚀

---

## 📞 STILL HAVING ISSUES?

If problems persist after following this guide:

1. **Check Terminal Output:** Look for specific error messages
2. **Check Browser Console:** Press F12, look for errors
3. **Verify File Locations:** Make sure all files are in the correct folders
4. **Try Restarting:** Close terminal, reopen, and run `python app.py` again

---

**Created by: Md Enaytullah**  
**Last Updated: October 21, 2025**  
**Status: ✅ COMPLETE & TESTED**
