import os
import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")

    else:
        speak("Good night")
    speak(" I am Sahejogi, please tell me how can I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        speak("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogniseing.....")
        speak("Recogniseing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : { query}\n")

    except Exception as e:
        print("say that again.")
        speak("say that again.")
        return "None"
    return query


def open_application(application_name):
    try:
        os.system(f'start "" "{application_name}"')
    except Exception as e:
        print(f"Error opening {application_name}: {e}")
        speak(f"Sorry, I encountered an error while opening {application_name}")


def close_application(application_name):
    try:
        os.system(f"TASKKILL /F /IM {application_name}.exe")
        speak(f"{application_name} has been closed")
    except Exception as e:
        print(f"Error closing {application_name}: {e}")
        speak(f"Sorry, I encountered an error while closing {application_name}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("searching wikkipedia....")
            query = query.replace("wilipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "close youtube" in query:
            os.system(
                "TASKKILL /F /IM brave.exe"
            )  # Assumes that YouTube is opened in Chrome. Adjust accordingly.

        elif "close google" in query:
            os.system(
                "TASKKILL /F /IM brave.exe"
            )  # Assumes that Google is opened in Chrome. Adjust accordingly.

        elif "close stackoverflow" in query:
            os.system(
                "TASKKILL /F /IM brave.exe"
            )  # Assumes that Stack Overflow is opened in Chrome. Adjust accordingly.

        elif "open" in query and "application" in query:
            # Extract application name from the query
            words = query.split()
            app_index = words.index("open") + 1
            application_name = " ".join(words[app_index:])
            open_application(application_name)

        elif "close" in query and "application" in query:
            # Extract application name from the query
            words = query.split()
            app_index = words.index("close") + 1
            application_name = " ".join(words[app_index:])
            close_application(application_name)

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strtime}\n")

        elif "exit" in query or "quit" in query:
            exit()

        else:
            print("Command not recognized.")
