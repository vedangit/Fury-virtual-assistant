import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
# speak("Good morning sunshine")

def takeCommand():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Analysing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: {}\n".format(query))
 
    except Exception:
        print("Say that again please...")  
        return "None"
    return query