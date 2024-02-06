import pygame
import tkinter
from tkinter import *
from pygame import mixer
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()#creating a window
player.title("Music Player")
player.geometry("1215x800")
player.configure(bg="#0f1a2c")
player.resizable(False,False)


mixer.init()#intializing the mixer

def open_folder():
    songlist=[]
    os.chdir(askdirectory())
    #seeking the permission to open folder in pc
    songlist = os.listdir()
    for song in songlist:
        if song.endswith(".mp3"):
            Playlist.insert(END,song)
                       #creating playlist


def play_song():
    music_name=Playlist.get(ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))#selecting song
    item=mixer.music.play()#playing song
    music.config(text=music_name[0:-4])#printing music name
icon=PhotoImage(file="logo.png")
player.iconphoto(False,icon)#displays icon on the top i.e at the heading

def prev():
    previous_one=Playlist.curselection()
    previous_one=previous_one[0]-1
    temp2=Playlist.get(previous_one)
    Playlist.activate(previous_one)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    Playlist.selection_clear(0,END)
    Playlist.selection_set(previous_one)
    music.config(text=temp2[0:-4])
    
def Nextt():
    next_one=Playlist.curselection()
    next_one=next_one[0]+1
    temp=Playlist.get(next_one)
    Playlist.activate(next_one)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    Playlist.selection_clear(0,END)
    Playlist.selection_set(next_one)
    music.config(text=temp[0:-4])

top=PhotoImage(file="top.png")
Label(player,image=top,bg="#0f1a2c").pack()# displays the top blue shade

logo=PhotoImage(file="logo.png")
Label(player,image=logo,bg="#0f1a2c",bd=0).place(x=250,y=100)

play=PhotoImage(file="play.png")
Button(player,image=play,bg="#0f1a2c",bd=0,command=play_song).place(x=130,y=500)

stop=PhotoImage(file="stop.png")
Button(player,image=stop,bg="#0f1a2c",bd=0,command=mixer.music.stop).place(x=250,y=500)

pause=PhotoImage(file="pause.png")
Button(player,image=pause,bg="#0f1a2c",bd=0,command=mixer.music.pause).place(x=10,y=500)

resume=PhotoImage(file="resume.png")
Button(player,image=resume,bg="#0f1a2c",bd=0,command=mixer.music.unpause).place(x=130,y=600)

previous=PhotoImage(file="previous.png")
Button(player,image=previous,bg="#0f1a2c",command=prev).place(x=10,y=600)

Next=PhotoImage(file="next.png")
Button(player,image=Next,bg="#0f1a2c",command=Nextt).place(x=250,y=600)

music=Label(player,text="",font=("black",15),fg="white",bg="#0f1a2c")
music.place(x=150,y=340,anchor="center") 

Menu=PhotoImage(file="menu.png")
Label(player,image=Menu,bg="#0f1a2c").pack(padx=80,pady=10,side=RIGHT)

Frame_Music = Frame(player, bd=2, relief = RIDGE)
Frame_Music.place(x=610, y=450, width=500, height=270)

Button(player, text="Open Folder", width=15, height=2, font=("algerian",12,"bold"),fg="Black", bg="#21b3de",command=open_folder).place(x=590, y=350)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("black",10), bg="#333333", fg="white", selectbackground="lightblue", cursor="hand2", bd=0,yscrollcommand=Scroll.set)

Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

player.mainloop
