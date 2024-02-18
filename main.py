import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query

if __name__ == '__main__':
    speak("Vivekananda assistance activated ")
    speak("How can I help you today sir?")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am vivek developed by Vivekananda")
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")
        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            loc = r"C:\Users\jaspr\AppData\Local\WhatsApp\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("Opening music")
            webbrowser.open("https://www.spotify.com")
        elif 'local disk d' in query:
            speak("Opening local disk D")
            os.startfile("D:")
        elif 'local disk c' in query:
            speak("Opening local disk C")
            os.startfile("C:")
        elif 'local disk e' in query:
            speak("Opening local disk E")
            os.startfile("E:")
        elif 'sleep' in query:
            exit(0)
