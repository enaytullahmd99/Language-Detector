"""
🔍 Language Detector App - Diagnostic Script
This script checks for common issues before running the app.
"""

import os
import sys

print("=" * 60)
print("🔍 LANGUAGE DETECTOR APP - DIAGNOSTIC CHECK")
print("=" * 60)
print()

# Check 1: Python Version
print("✓ Checking Python version...")
print(f"  Python {sys.version}")
if sys.version_info < (3, 8):
    print("  ⚠️ WARNING: Python 3.8+ recommended")
else:
    print("  ✅ Python version OK")
print()

# Check 2: Required Modules
print("✓ Checking required modules...")
required_modules = ['flask', 'joblib', 'regex', 'sklearn', 'pandas', 'numpy']
missing_modules = []

for module in required_modules:
    try:
        if module == 'sklearn':
            __import__('sklearn')
        else:
            __import__(module)
        print(f"  ✅ {module:15} - Installed")
    except ImportError:
        print(f"  ❌ {module:15} - NOT FOUND")
        missing_modules.append(module)

if missing_modules:
    print(f"\n  ⚠️ Missing modules: {', '.join(missing_modules)}")
    print(f"  Run: pip install {' '.join(missing_modules)}")
else:
    print("\n  ✅ All required modules installed")
print()

# Check 3: Required Files
print("✓ Checking required files...")
required_files = [
    'app.py',
    'templates/index.html',
    'SVM_model.pkl',
    'tfidf_vectorizer.pkl'
]

all_files_present = True
for file in required_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"  ✅ {file:30} ({size:,} bytes)")
    else:
        print(f"  ❌ {file:30} NOT FOUND")
        all_files_present = False

if not all_files_present:
    print("\n  ⚠️ Some required files are missing!")
    print("  Make sure you're running this from the app directory")
else:
    print("\n  ✅ All required files present")
print()

# Check 4: Model Loading Test
print("✓ Testing model loading...")
try:
    import joblib
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('SVM_model.pkl')
    print("  ✅ Model and vectorizer loaded successfully")
except Exception as e:
    print(f"  ❌ Failed to load models: {e}")
print()

# Check 5: Port Availability
print("✓ Checking if port 5000 is available...")
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1', 5000))
if result == 0:
    print("  ⚠️ Port 5000 is already in use")
    print("  You may need to stop other applications or change the port")
else:
    print("  ✅ Port 5000 is available")
sock.close()
print()

# Check 6: Test Prediction
print("✓ Testing prediction functionality...")
try:
    import regex as re
    
    def clean_input(text):
        if not isinstance(text, str):
            return ""
        text = re.sub(r"[^\p{L}\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    test_text = "Hello, how are you?"
    cleaned = clean_input(test_text)
    X_test = vectorizer.transform([cleaned])
    prediction = model.predict(X_test)[0]
    print(f"  ✅ Test prediction: '{test_text}' → {prediction}")
except Exception as e:
    print(f"  ❌ Prediction test failed: {e}")
print()

# Final Summary
print("=" * 60)
print("📊 DIAGNOSTIC SUMMARY")
print("=" * 60)

if not missing_modules and all_files_present:
    print("✅ ALL CHECKS PASSED!")
    print()
    print("🚀 Your app is ready to run!")
    print()
    print("To start the server:")
    print("  python app.py")
    print()
    print("Then open your browser to:")
    print("  http://127.0.0.1:5000")
else:
    print("⚠️ SOME ISSUES FOUND")
    print()
    if missing_modules:
        print("1. Install missing modules:")
        print(f"   pip install {' '.join(missing_modules)}")
    if not all_files_present:
        print("2. Make sure you're in the correct directory")
        print("   cd \"c:\\Users\\enayt\\Desktop\\Enayat\\Language Detector App\"")
    print()
    print("After fixing, run this diagnostic again")

print("=" * 60)
