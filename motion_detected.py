from Tkinter import *
import tkMessageBox
import vlc

media = vlc.MediaPlayer("/home/pi/Pimoroni/speakerphat/test/test.mp3")
media.play()
tkMessageBox.showinfo("Motion Detected!", "Hello World")
