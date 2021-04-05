
import pygame
from pygame import mixer
from tkinter import *
import os

# def playnext():

#     nextsong = 

def playing():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root = Tk()
root.title("Gaurav's Music Player")

mixer.init()
songstatus = StringVar()
songstatus.set("Choosing")

#playist.
playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Lenovo\Desktop\MyPlaylist')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root,text="play",command=playing)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

stopbtn = Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn = Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()

# playist = Listbox(root, selectmode=SINGLE,bg="DodgerBlue2",fg=)
