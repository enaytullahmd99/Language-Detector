"""Quick API test script"""
import urllib.request
import json

# Test the /predict endpoint
url = "http://127.0.0.1:5000/predict"
data = {"text": "Bonjour, comment allez-vous?"}

try:
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"Status Code: {response.status}")
        print(f"Response: {result}")
except Exception as e:
    print(f"Error: {e}")
