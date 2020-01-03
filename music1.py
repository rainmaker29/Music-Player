import os
from tkinter.filedialog import askdirectory
from mutagen.mp3 import MP3
import pygame
from mutagen.id3 import ID3,ID3NoHeaderError
from tkinter import *
import tkinter.ttk as ttk

from ttkthemes import ThemedStyle


root = Tk()
root.minsize(300,300)
root.title("rainmaker's player")


style = ThemedStyle(root)
style.set_theme("scidgrey")



listofsongs = []

realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

counter = 0
def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            

            realdir = os.path.realpath(files)


            audio = ID3(realdir)

            realnames.append(audio['TIT2'].text[0])

#            realnames.append(audio.tags)
           
            listofsongs.append(files)
           
    
    pygame.mixer.init(frequency=50050)
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def playsong(event):
    global index
    pygame.mixer.music.unpause()
def pausesong(event):
    pygame.mixer.music.pause()


def change_vol(_=None):
    pygame.mixer.music.set_volume(vol.get())


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = Label(root,text='  ')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = ttk.Button(root,text = 'Next Song')
nextbutton.pack()

label2 = Label(root,text='  ')
label2.pack()


previousbutton =ttk. Button(root,text = 'Previous Song')
previousbutton.pack()


label3 = Label(root,text='  ')
label3.pack()


stopbutton = ttk.Button(root,text = 'Stop Music')
stopbutton.pack()

label4 = Label(root,text='  ')
label4.pack()


playbutton = ttk.Button(root,text = "PLay music")
playbutton.pack()

label5 = Label(root,text='  ')
label5.pack()


pausebutton = ttk.Button(root,text = "Pause")
pausebutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong)
pausebutton.bind("<Button-1>",pausesong)

vol = Scale(
    root,
    from_ = 0,
    to = 1,
    orient = HORIZONTAL ,
    resolution = .1,
    ####################
    command=change_vol
    ####################
)

label6 = Label(root,text='  ')
label6.pack()


vol.pack()

label9 = Label(root,text='  ')
label9.pack()

songlabel.pack()

root.mainloop()
