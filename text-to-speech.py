import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox 
import pyttsx3
import os



root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender = gender_Combobox.get()
    speed= speed_gender_Combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text=text_area.get(1.0,END)
    gender = gender_Combobox.get()
    speed= speed_gender_Combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if (text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

# icon
image_icon=PhotoImage(file="speak_7642748.png")
root.iconphoto(False,image_icon)

# top frame
Top_frame=Frame(root,bg="white",width=900, height =100)
Top_frame.place(x=0,y=0)

logo=PhotoImage(file="speaker.png")
Label(Top_frame,image=logo,bg="white").place(x=10,y=5)

Label(Top_frame, text="Text To Speech", font="arial 20 bold", bg="white",fg="black").place(x=100,y=30)

# 

text_area=Text(root, font="Robote 20", bg="white",relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150,width=500, height=250)

Label(root,text="VOICE", font="arial 15 bold", bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED", font="arial 15 bold", bg="#305065",fg="white").place(x=760,y=160)

gender_Combobox=Combobox(root, values=['Male','Female'], font="arial 14",state='r',width=10)
gender_Combobox.place(x=550,y=200)
gender_Combobox.set('Male')

speed_gender_Combobox=Combobox(root, values=['Fast','Normal','Slow'], font="arial 14",state='r',width=10)
speed_gender_Combobox.place(x=730,y=200)
speed_gender_Combobox.set('Normal')

imageicon=PhotoImage(file="speak_7642748.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon, width=170,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="down-arrow_17412294 (1).png")
save=Button(root,text="Download",compound=LEFT,image=imageicon2, width=170,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=740,y=280)







root.mainloop()