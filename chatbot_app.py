import nltk
from nltk.chat.util import Chat, reflections
import streamlit as st
import speech_recognition as sr

# Sample chatbot pairs (can be expanded)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! Ask me anything."]
    ],
    [
        r"what is your name ?",
        ["I'm your voice-enabled chatbot!", "You can call me ChatBuddy."]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBuddy.", "I'm just a simple chatbot."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to answer that. Can you try asking something else?"]
    ]
]

chatbot = Chat(pairs, reflections)

# 🗣️ Function to transcribe speech
def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("🎤 Listening... Please speak clearly.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"📝 Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        st.error(f"❌ Google API Error: {e}")
        return ""

# Streamlit App
def main():
    st.title("🧠 ChatBuddy: Text & Voice Chatbot")
    st.write("Talk to the chatbot by typing or using your microphone 🎙️")

    input_mode = st.radio("Choose input mode:", ("Text", "Voice"))

    if input_mode == "Text":
        user_input = st.text_input("💬 Type your message:")

        if user_input:
            response = chatbot.respond(user_input)
            st.text_area("🤖 Chatbot response:", value=response, height=100)

    elif input_mode == "Voice":
        if st.button("🎙️ Click to speak"):
            speech_text = transcribe_speech()
            if speech_text:
                response = chatbot.respond(speech_text)
                st.text_area("🤖 Chatbot response:", value=response, height=100)

if __name__ == "__main__":
    main()
