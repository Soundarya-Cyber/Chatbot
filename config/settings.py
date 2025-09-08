# config/settings.py

# ⚠️ Put your real Gemini API key here
GEMINI_API_KEY = "AIzaSyCMMzvmmKQ_DTxDNf39A8dBESbkmyi6uK4"

if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_ACTUAL_GEMINI_API_KEY":
    raise ValueError("⚠️ Please update settings.py with your actual Gemini API key.")
