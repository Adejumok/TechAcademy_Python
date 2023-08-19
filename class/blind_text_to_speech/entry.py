import pyttsx3  # install pyttsx3

import speech_recognition as sr  # install speechrecognition


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
r = sr.Recognizer()


def speak(text):
    # Function to convert text to speech
    engine.say(text)
    engine.runAndWait()


def listen():
    # Function to listen to user's voice input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None




    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


