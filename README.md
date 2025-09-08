🤖 Iron Lady Chatbot

A simple Streamlit-based chatbot that answers questions related to Iron Lady’s leadership programs.
The chatbot uses:

Predefined FAQs for quick answers.

Google Gemini API (gemini-2.5-pro) for intelligent, conversational responses.

Chat history to maintain context between user and bot.

📂 Project Structure
chatbot/
│── app.py                # Main Streamlit app
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│
├── config/
│   └── settings.py       # API key configuration
│
└── utils/
    └── chatbot.py        # FAQ handling & Gemini API calls

⚡ Features

✅ Answers predefined FAQs about Iron Lady programs
✅ Uses Gemini AI for conversational replies
✅ Maintains chat history for multi-turn conversations
✅ Built with Streamlit for a clean web UI

🔑 Setup
1. Clone this repo
git clone https://github.com/your-username/ironlady-chatbot.git
cd ironlady-chatbot

2. Install dependencies
pip install -r requirements.txt

3. Add your Gemini API key

Open config/settings.py and replace with your actual key:

GEMINI_API_KEY = "YOUR_API_KEY_HERE"


If you don’t have one, get it from Google AI Studio
.

4. Run the app
streamlit run app.py

🎯 Example Questions

What programs does Iron Lady offer?

What is the program duration?

Is the program online or offline?

Are certificates provided?

Who are the mentors/coaches?

📸 Screenshot

(Optional: Add a screenshot of your chatbot UI here)

📜 License

This project is for educational/demo purposes.