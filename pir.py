#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import time
import requests
import vlc
import random

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
pinpir = 17

# Set GPIO pin as input
GPIO.setup(pinpir, GPIO.IN)

# Variables to hold the current and last states
currentstate = 0
previousstate = 0

try:
	print("Waiting for PIR to settle ...")

	# Loop until PIR output is 0
	while GPIO.input(pinpir) == 1:

		currentstate = 0

	print("    Ready")

	# Loop until users quits with CTRL-C
	while True:

		# Read PIR state
		currentstate = GPIO.input(pinpir)

		# If the PIR is triggered
		if currentstate == 1 and previousstate == 0:

			print("Motion detected!")
		#Generate a Random Integer
			x = random.randint(1,10)
			song = '/home/pi/Handwashing_Timer_Music/music/'+ str(x) +'.mp3'
		# VLC player on motion

			media = vlc.MediaPlayer(song)
			media.play()
			# Record new previous state
			previousstate = 1
			#Wait 120 seconds before looping again
			print("Waiting 30 seconds")
			time.sleep(30)

		# If the PIR has returned to ready state
		elif currentstate == 0 and previousstate == 1:

			print("Ready")
			previousstate = 0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	print("    Quit")

	# Reset GPIO settings
	GPIO.cleanup()
