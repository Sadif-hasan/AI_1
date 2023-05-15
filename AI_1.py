from datetime import datetime

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import random

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define the function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define the function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Can you please repeat?")
            return recognize_speech()

# Define the main function to execute commands
def execute_command():
    command = recognize_speech()
    if "open" in command:
        if "google" in command:
            webbrowser.open("https://www.google.com")
        elif "youtube" in command:
            webbrowser.open("https://www.youtube.com")
        elif "github" in command:
            webbrowser.open("https://github.com")
        else:
            speak("Sorry, I can't open that website.")
    elif "play music" in command:
        music_dir = "C:/Users/Username/Music"
        songs = os.listdir(music_dir)
        song = random.choice(songs)
        os.startfile(os.path.join(music_dir, song))
    elif "what time is it" in command:
        speak("The time is " + datetime.datetime.now().strftime("%H:%M"))
    elif "how are you" in command:
        speak("I'm doing well, thank you for asking!")
    elif "weather" in command:
        webbrowser.open("https://www.msn.com/en-us/weather/forecast")
    else:
        speak("Sorry, I didn't understand that command. Can you please repeat?")

# Start the voice assistant
speak("Hello, how can I help you?")
while True:
    execute_command()
