import speech_recognition as sr
import spacy
from datetime import datetime
import webbrowser
import os

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize spaCy for natural language processing
nlp = spacy.load("en_core_web_sm")


def process_text(text):
    doc = nlp(text)

    # Basic commands
    if "open" in text:
        # Extract the entity following "open"
        entity = [token.text for token in doc if token.dep_ == "dobj"]
        if entity:
            webbrowser.open(f"https://www.google.com/search?q={entity[0]}")
        else:
            print("Could not identify what to open.")

    elif "what is the time" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"The current time is {current_time}.")

    elif "search" in text:
        # Extract the query following "search"
        query = " ".join([token.text for token in doc if token.dep_ == "dobj"])
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            print("Could not identify what to search.")

    elif "exit" in text or "quit" in text:
        exit()

    else:
        print("Command not recognized.")


def listen_and_process():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            process_text(text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}"
            )


if __name__ == "__main__":
    while True:
        listen_and_process()
