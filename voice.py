import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("🎤 Say something...")
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    # Capture audio
    audio = recognizer.listen(source)

try:
    # Convert speech to text using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("📝 You said: " + text)
except sr.UnknownValueError:
    print("❌ Sorry, I could not understand the audio.")
except sr.RequestError:
    print("⚠️ Could not request results; check your internet connection.")