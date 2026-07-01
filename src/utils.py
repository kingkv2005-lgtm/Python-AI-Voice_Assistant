import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


def get_current_date():
    today = datetime.datetime.now()
    return today.strftime("%d-%m-%Y")


def search_web():
    speak("Please say the topic to search")

    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for topic...")

            audio = recognizer.listen(source, timeout=8)
            topic = recognizer.recognize_google(audio).lower()

            print("Searching Google for:", topic)

            url = f"https://www.google.com/search?q={topic.replace(' ','+')}"
            webbrowser.open(url)

            speak(f"Searching Google for {topic}")

        except:
            speak("Sorry I couldn't understand the topic")


def search_youtube():
    speak("Please say the topic to search")

    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for topic...")

            audio = recognizer.listen(source, timeout=10)
            topic = recognizer.recognize_google(audio).lower()

            print("Searching YouTube for:", topic)

            url = f"https://www.youtube.com/results?search_query={topic.replace(' ','+')}"
            webbrowser.open(url)

            speak(f"Searching YouTube for {topic}")

        except:
            speak("Sorry I couldn't understand the topic")
