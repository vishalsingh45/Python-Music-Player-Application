#importing necessary modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#Creating app Window
musicplayer=tkr.Tk()

#setting the tile name
musicplayer.title("Music Player")

#setting the dimensions
musicplayer.geometry("450x350")

#asking for music directory
directory=askdirectory()

#set music dir to current working dir
os.chdir(directory)

#creating song list
#os.listdir() return the list containing the names of songs in the dir given by the path
songlist=os.listdir()

#creating the playlist
playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg="cyan2", selectmode = tkr.SINGLE)

#adding songs from songlist to the play list
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1

#initializing modules
pygame.init()
pygame.mixer.init()

#fuction for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#fuction for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()

#fuction for pause button
def pause():
     pygame.mixer.music.pause()

#fuction for resume button
def resume():
    pygame.mixer.music.unpause()

#Creating buttons
Button1 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold", text="Play Music", command=play, bg="cadetblue", fg="black")
Button2 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold", text="Stop Music", command=ExitMusicPlayer, bg="orchid", fg="black")
Button3 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 16 bold", text="Pause Music", command=pause, bg="dimgrey", fg="black")
Button4 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 16 bold", text="Resume Music", command=resume, bg="navy", fg="black")

var = tkr.StringVar()

songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)
songtitle.pack()

Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()