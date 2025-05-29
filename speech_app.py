import speech_recognition as sr



def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Speak now...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("📝 Transcription:")
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ Google API Error: {e}")

if __name__ == "__main__":
    main()
