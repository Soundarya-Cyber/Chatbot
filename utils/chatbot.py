from config.settings import GEMINI_API_KEY
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Predefined FAQs
FAQS = {
    "What programs does Iron Lady offer?": "Iron Lady offers leadership programs such as Women Leadership Accelerator, Executive Presence, and Career Growth Bootcamp.",
    "What is the program duration?": "Program durations vary: Accelerators are typically 8-12 weeks, Bootcamps are 4-6 weeks.",
    "Who can join Iron Lady programs?": "Women professionals, leaders, and aspiring managers who want to accelerate their career growth.",
    "Is the program online or offline?": "Most Iron Lady programs are conducted online with live interactive sessions."
}

def get_faq_answer(query: str):
    """Check if the query matches predefined FAQs."""
    for question, answer in FAQS.items():
        if query.lower() in question.lower():
            return answer
    return None

def ask_gemini(query: str):
    """Send user query to Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(query)
        return response.text if response else "Sorry, I couldn’t get a response."
    except Exception as e:
        return f"⚠️ Error: {e}"
