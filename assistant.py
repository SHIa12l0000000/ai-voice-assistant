import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit
from config import ask_openai

# Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("🧠 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("🗣️ You:", query)
        return query
    except:
        speak("Sorry, I didn't understand.")
        return ""

def handle_command(query):
    query = query.lower()

    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "date" in query:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date}")

    elif "play" in query:
        song = query.replace("play", "")
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")

    elif "exit" in query or "stop" in query:
        speak("Goodbye!")
        return False

    else:
        response = ask_openai(query)
        speak(response)

    return True
  
