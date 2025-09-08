import streamlit as st
from utils.chatbot import get_faq_answer, ask_gemini

st.set_page_config(page_title="Iron Lady Chatbot", page_icon="🤖")

st.title("🤖 Iron Lady Chatbot")
st.write("Ask me about Iron Lady's programs:")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_query = st.text_input("Type your question here:")

if user_query:
    # First check FAQs
    faq_answer = get_faq_answer(user_query)
    if faq_answer:
        bot_response = faq_answer
    else:
        with st.spinner("Thinking..."):
            bot_response = ask_gemini(user_query)

    # Save chat to history
    st.session_state.history.append({"user": user_query, "bot": bot_response})

# Display chat history
if st.session_state.history:
    st.subheader("💬 Chat History")
    for chat in st.session_state.history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Bot:** {chat['bot']}")
        st.write("---")
