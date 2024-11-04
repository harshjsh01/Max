#from re import I
from tkinter import *
import pyttsx3 
#import speech_recognition as sr
import datetime
import urllib.request
import cv2
import numpy as np
import time
import wikipedia
import webbrowser
import os
from datetime import date
import random
from tkinter import messagebox
import speedtest
from function import speak
from function import wishMe
from function import takecommand
from function import ext
from function import alarm
import pyautogui
from pyautogui import click 
from keyboard import write
from function import whatappmsg
from function import whatappcall
from function import whatappvcall
import openai

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

class MaxAI:
    def __init__(self, name="Max"):
        self.name = name

    def chat_with_gpt(self, prompt):
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

st = date.today().strftime("%d-%m-%Y")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def come():
    if __name__ == "__main__":
        wishMe()
        while True:
            print("\n\n")
            query = takecommand().lower()
            #this is for random number picking
            n = random.randint(0,16)
            
            if "wikipedia" in query:
                    print("Ok Sir!")
                    speak("Ok Sir!")
                    speak("searching wikipedia sir")
                    query = query.replace("wikipedia","")
                    query = query.replace("search","")
                    query = query.replace("max","")
                    re = wikipedia.summary(query,sentences=5)
                    speak("according to wikipedia")
                    speak(re)
                    messagebox.showinfo("According to Wikipedia",re)
                    
            elif "open youtube" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening youtube sir")
                webbrowser.open("youtube.com")

            elif "search on google" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("searching on google sir")
                query = query.replace("search on google","")
                query = query.replace("max","")
                webbrowser.open(query)

            elif "open google" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening google sir")
                webbrowser.open("google.com")

            elif "open stackoverflow" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening stackoverflow sir")
                webbrowser.open("stackoverflow.com")

            elif "play music" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("playing music sir")
                iron = "./music"
                songs = os.listdir(iron)
                os.startfile(os.path.join(iron,songs[n]))

            elif "time" in query:
                st = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is {st}")

            elif "open code" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening code sir")
                code = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(code)

            elif "who are you" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                print("I am Max")
                speak("I am Max")
                print("I am artificial intelligence Program")
                speak("I am artificial intelligence program")
                print("As Asistant of User")
                speak("As Asistant of User")

            elif "who make you" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                print("HARSH JOSHI had made Me")
                speak("HARSH JOSHI had made me")
                print("He is my first BOSS")
                speak("He is my first BOSS")

            elif "what do you do" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                print("I hlep you in runing computer")
                speak("I hlep you in runing computer")

            elif "quit" in query  or "go to sleep" in query or "exit" in query or "need a break" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("Exiting Program sir")
                exit()

            elif "search on youtube" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                query = query.replace("search on youtube","")
                query = query.replace("max","")
                speak("Searching on YouTube sir")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

            elif "date" in query:
                st = date.today()
                print(st)
                speak(f"sir the date is {st}")

            elif "open command " in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening sir")
                os.startfile("C:\\Windows\\System32\\cmd.exe")

            elif "open firefox" in query:
                print("Ok Sir!")
                speak("Ok Sir!")
                speak("opening sir")
                os.startfile("C:\\Users\\Public\\Desktop\\Firefox.lnk")

            elif "are you there" in query:
                speak("I am alway there for you sir")

            elif "wake up" in query:
                speak("I am already wakup sir")

            elif "thank you" in query:
                speak("your welcome sir")

            elif "facebook" in query:
                print("ok sir")
                speak("ok sir")
                webbrowser.open("facebook.com")

            elif "instagram" in query:
                print("ok sir")
                speak("ok sir")
                webbrowser.open("instagram.com")

            elif "twitter" in query:
                print("ok sir")
                speak("ok sir")
                webbrowser.open("twitter.com")
            
            elif "send message" in query:
                query = query.replace("send message to","")
                query = query.replace("max","")
                speak("what you want to send")
                bc = takecommand()
                whatappmsg(name=query,message=bc)

            elif "video call" in query:
                query = query.replace("call","")
                query = query.replace("max","")
                query = query.replace("video","")
                speak(f"calling {query}")
                whatappvcall(name=query)

            elif "call" in query:
                query = query.replace("call","")
                query = query.replace("max","")
                speak(f"calling {query}")
                whatappcall(name=query)

            elif "location of renu" in query:
                speak("ok sir")
                print("ok sir")
                speak("showing sir")
                webbrowser.open("https://maps.app.goo.gl/zBbC12WkGVyTapym8")
            
            elif "location of sunil" in query:
                speak("ok sir")
                print("ok sir")
                speak("showing sir")
                webbrowser.open("https://maps.app.goo.gl/PMB3HGyoQnbNVea38")

            elif "location of harsh" in query:
                speak("ok sir")
                print("ok sir")
                speak("showing sir")
                webbrowser.open("https://www.google.com/maps/@28.1301659,75.3981325,174m/data=!3m1!1e3!13s111988005419150522433")
                
            elif "add folder in private" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add folder in private name as ","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.makedirs(f"C:\\Users\\anonemous\\Documents\\Private\\{query}")

            elif "remove folder from private" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove folder from private name as ","")
                os.removedirs(f"C:\\Users\\anonemous\\Documents\\Private\\{query}")

            elif "add folder in documents" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add folder in documents name as ","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.makedirs(f"C:\\Users\\anonemous\\Documents\\{query}")

            elif "remove folder from documents" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove folder from documents name as ","")
                os.removedirs(f"C:\\Users\\anonemous\\Documents\\{query}")

            elif "add python file" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add","")
                query = query.replace("python","")
                query = query.replace("file","")
                query = query.replace("name","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.chdir("C:\\Users\\anonemous\\Documents\\python")
                open(f"{query}.py","w+")

            elif "add python file in private" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add python file in private name as","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.chdir("C:\\Users\\anonemous\\Documents\\Private")
                open(f"{query}.py","w+")

            elif "add folder on desktop" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add folder on desktop name ","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.makedirs(f"C:\\Users\\anonemous\\Desktop\\{query}")

            elif "remove folder from desktop" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove folder from desktop name as ","")
                os.removedirs(f"C:\\Users\\anonemous\\Desktop\\{query}")

            elif "add text file" in query:
                speak("ok sir")
                print("ok sir")
                speak("creating sir")
                query = query.replace("add text file name as","")
                query = query.replace("as","")
                query = query.replace("is","")
                os.chdir("C:\\Users\\anonemous\\Documents")
                open(f"{query}.txt","w+")

            elif "shut down" in query or "power off" in query:
                speak("ok sir")
                print("ok sir")
                speak("shuting down sir")
                os.system("shutdown /s /t 1")

            elif "remove python file from private" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove python file from private name as","")
                os.chdir("C:\\Users\\anonemous\\Documents\\Private")
                os.remove(f"{query}.py")

            elif "remove python file" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove python file name as","")
                os.chdir("C:\\Users\\anonemous\\Documents")
                os.remove(f"{query}.py")

            elif "remove text file" in query:
                speak("ok sir")
                print("ok sir")
                speak("removing sir")
                query = query.replace("remove text file name as","")
                os.chdir("C:\\Users\\anonemous\\Documents")
                os.remove(f"{query}.txt")

            elif "show documents" in query:
                speak("ok sir")
                speak("showing sir")
                os.startfile("C:\\Users\\anonemous\\Documents")

            elif "show downloads" in query:
                speak("ok sir")
                speak("showing sir")
                os.startfile("C:\\Users\\anonemous\\Downloads")

            elif "close instagram" in query or "close twiter" in query or "close facebook" in query or "close browser" in query or "close google" in query or "close youtube" in query or "close firefox" in query:
                speak("ok sir")
                speak("closing sir")
                os.system("taskkill /im firefox.exe /f")

            elif "close code" in query:
                speak("ok sir")
                speak("closing sir")
                webb = "Code.exe"
                os.system("taskkill /im Code.exe /f")

            elif "close command" in query:
                speak("ok sir")
                speak("closing sir")
                os.system("taskkill /im cmd.exe /f")

            elif "stop music" in query:
                speak("ok sir")
                speak("closing sir")
                os.system("taskkill /im wmplayer.exe /f")

            elif "write" in query:
                speak("ok sir")
                query = query.replace("write","")
                write(query)

            elif "check" in query and "speed" in query:
                speak("ok sir")
                speak("checking speed sir")
                speed = speedtest.Speedtest()
                downloading = speed.download()
                codown = int(downloading/800000)
                uploading = speed.upload()
                coup = int(uploading/800000)
                if "uploading" in query or "upload" in query:
                    speak(f"sir the uploading speed is {coup}m b p s")

                elif "downloading" in query or "download" in query:
                    speak(f"sir the downloading speed is {codown}m b p s")

                elif "internet" in query:
                    speak(f"sir the uploading speed is {coup}m b p s")
                    speak("and")
                    speak(f" the downloading speed is {codown}m b p s")

            elif "run alarm" in query:
                alarm()

            elif "door camera" in query:
                URL = "http://192.168.43.149:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;

                cv2.destroyAllWindows()

            elif "volume up" in query:
                pyautogui.press("volumeup")

            elif "volume down" in query:
                pyautogui.press("volumedown")

            elif "mute" in query:
                pyautogui.press("volumemute")
            
            elif "hi" in query:
                speak("hi sir")

            elif "hello"in query:
                speak("hello sir")
            else:
                speak(max.chat_with_gpt(query))

            


root = Tk()
root.title("MAX")
root.geometry("1280x800")
root.configure(background = "#000000")
frames = [PhotoImage(file='./guimage/jayshriram.gif',format = 'gif -index %i' %(i)) for i in range(41)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind > 40:
        ind = 0
    label.configure(image=frame)
    root.after(100,update,ind)

label = Label(root,relief="solid")
label.pack()
root.after(0,update,0)

root.attributes("-alpha",0.4)

image = PhotoImage(file ="./guimage/max2.png")
label1 = Label(root,image = image,bd = 0).place(x=0,y=0)

image1 = PhotoImage(file ="./guimage/max2.png")
label2 = Label(root,image = image1,bd = 0).place(x=1040,y=0)

image2 = PhotoImage(file ="./guimage/logor.png")
label3 = Label(root,image = image2,bd = 0).place(x=1065,y=520)

image3 = PhotoImage(file="./guimage/brain.png")
label4 = Label(root,image=image3,bd=0).place(x=0,y=500)

image4 = PhotoImage(file="./guimage/target.png")
label5 = Label(root,image=image4,bd=0).place(x=315,y=500)

image5 = PhotoImage(file="./guimage/percent.png")
label6 = Label(root,image=image5,bd=0).place(x=699,y=500)

clbtn = PhotoImage(file = "./guimage/exit3.png")
imag_label = Label(image = clbtn)
button = Button(root,image = clbtn,command= ext,borderwidth=0,highlightthickness=0).place(x=840, y=420)

imag = PhotoImage(file="./guimage/mic2.png")
labelimag = Label(image = imag)
button2 = Button(root,image = imag,command=come,borderwidth=0,highlightthickness=0).place(x=560,y=340)

image6 = PhotoImage(file="./guimage/h5.png")
label7 = Label(root,image=image6,bd=0,bg="black",fg="white",text=f"{st}",font = ('Garamond',20),compound=CENTER).place(x=520,y=0)

root.mainloop()
    

    