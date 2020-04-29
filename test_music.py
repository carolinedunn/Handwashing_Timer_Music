 
from Tkinter import *
import tkMessageBox
import vlc
import random


x = random.randint(1,10)
song = '/home/pi/Music/' + str(x) + '.mp3'
media = vlc.MediaPlayer(song)
#media = vlc.MediaPlayer("/home/pi/Pimoroni/speakerphat/test/test.mp3")
media.play()
tkMessageBox.showinfo("Motion Detected!", "Hello World")
