import pyttsx3 
import speech_recognition as sr
import datetime
from datetime import date
from re import I
import os
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep




#this is for seeing date 
st = date.today().strftime("%d-%m-%Y")

#this is for inporting voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takealarm():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        
        return "None"
    return query

#this is for wishing 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else :
        speak("Good Evening Sir!")

    speak("How may I help you")

#this is for converting speech to text
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        speak("not Recognizing")
        
        return "None"
    return query

def ext():
    exit()


def alarm():
    while True:
        query = takealarm().lower()
        ab = datetime.datetime.now().strftime("%H:%M:%S")
        if "shut down alarm" in query or "stop alarm" in query:
            speak("ok sir")
            os.system("taskkill /im wmplayer.exe /f")
            wishMe()
            break

        elif ab == "08:15:01":
            os.system("taskkill /im wmplayer.exe /f")
            break

        elif ab =="08:00:01" :
            iron = "./alarm"
            songs = os.listdir(iron)
            os.startfile(os.path.join(iron,songs[0]))

        else :
            ac=1

def whatappmsg(name,message):
    os.startfile("C:\\Users\\sunil\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(30)
    click(x=130,y=105)
    write(name)
    sleep(3)
    click(x=227, y=244)
    sleep(2)
    click(x=635, y=734)
    sleep(1)
    write(message)
    press("Enter")

def whatappcall(name):
    os.startfile("C:\\Users\\sunil\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(30)
    click(x=130,y=105)
    write(name)
    sleep(3)
    click(x=227, y=244)
    sleep(2)
    click(x=1123, y=54)

def whatappvcall(name):
    os.startfile("C:\\Users\\sunil\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(30)
    click(x=130,y=105)
    write(name)
    sleep(3)
    click(x=227, y=244)
    sleep(2)
    click(x=1076, y=59)

