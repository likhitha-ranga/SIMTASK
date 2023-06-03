import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
name = input("enter name")
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning"+name)
    elif hour >=12 and hour < 16:
        speak("good afternoon"+name)
    else:
        speak("good evening"+name)
    speak("I am chitti How may i help you?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query
print("Initialising chitti")
wishMe()
a=1
while(a):
    query=takeCommand()
    if "wikipedia" in query.lower():
        speak("searching wikipedia...")
        query=query.replace("Wikipedia"," ")
        print(query)
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
    elif "open youtube" in query.lower():
        query = query.replace("open YouTube", " ")
        url="https://www.youtube.com/results?search_query="+query
        webbrowser.open(url)
    elif "play music" in query.lower():
        songs_dir="C:\\Users\\ranga\\Downloads"
        songs=os.listdir("C:\\Users\\ranga\\Downloads")
        os.startfile(os.path.join(songs_dir,songs[4]))
    elif "the time" in query.lower():
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strtime)
        speak(f"{name}the time is{strtime}")
    elif "send message" in query.lower():
        pywhatkit.sendwhatmsg("+919876543210","Message",19,45)
    elif "exit" in query.lower():
        a=0

