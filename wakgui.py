from tkinter import *





import os
import speech_recognition as sr


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
        print("not recognize")
        return "None"

    return query


def wakup():
    while True:

        wak = takecommand().lower()

        if "wake up " in wak:
            a = os.startfile("C:\\Program Files\\MAX\\Max.py")
            exit()
            break

        elif "need your help " in wak:
            a = os.startfile("C:\\Program Files\\MAX\\Max.py")
            exit()
            break

        elif "start" in wak:
            a = os.startfile("C:\\Program Files\\MAX\\Max.py")
            exit()
            break

        elif "let's go" in wak:
            a = os.startfile("C:\\Program Files\\MAX\\Max.py")
            exit()
            break

    return a


root = Tk()

#for giving title
root.title("startup")

#this is for fix size and where to display
root.geometry("320x200+950+0")
# this comand is use colour the background :root.configure(background = "#000080")
#This is for removing border of main gui
root.overrideredirect(True)
#This is for transparent gui
root.attributes("-alpha",0.3)

#This is for puting background in gui
bg = PhotoImage(file ="./guimage/image1.png")
background = Label(root,image = bg,bd = 0)
background.pack()

#THis is for creating exit button
clbtn = PhotoImage(file = "./guimage/exit.png")
#a = Frame(root, background="#001a66")
imag_label = Label(image = clbtn)
button = Button(root,image = clbtn,command= exit,borderwidth=0,highlightthickness=0).place(x=250, y=175)
#button.pack(pady = 30)

#This is for creating start button 
abcde = PhotoImage(file = "./guimage/mic.png")
imag_label2 = Label(image = abcde)
button2 = Button(root,image = abcde,command=wakup,borderwidth=0,highlightthickness=0).place(x=150,y=86)


root.mainloop()



