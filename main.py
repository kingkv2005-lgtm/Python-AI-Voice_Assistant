import speech_recognition as sr
from utils import speak, get_current_time, get_current_date, search_web, search_youtube

recognizer = sr.Recognizer()


def listen_and_respond():

    with sr.Microphone() as source:

        print("Jarvis is listening (say exit to stop)")
        recognizer.adjust_for_ambient_noise(source)

        while True:

            try:
                print("\nListening...")

                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio).lower()

                print("You said:", text)

                if "your name" in text:
                    speak("My name is Jarvis")


                elif any(word in text for word in ["time", "clock"]):
                    speak(f"The time is {get_current_time()}")


                elif any(word in text for word in ["date", "today"]):
                    speak(f"Today's date is {get_current_date()}")

                elif "search web" in text:
                    search_web()

                elif "search youtube" in text:
                    search_youtube()

                elif "exit" in text:
                    speak("Goodbye")
                    break

                else:
                    speak("I heard you but I don't understand")

            except sr.UnknownValueError:
                print("Could not understand")

            except sr.WaitTimeoutError:
                print("No speech detected")

            except sr.RequestError:
                print("Internet error")


listen_and_respond()
