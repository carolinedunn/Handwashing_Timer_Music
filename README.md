# Handwashing_Timer_Music
Raspberry Pi with Pimoroni Speaker Phat and motion sensor that plays a 20 second song to indicate length of hand washing.
NOTE: This is a SOLDERING project! I do not recommend this project for someone without prior soldering experience.

# Materials
Raspberry Pi Zero W, 3 or 4
PIR Motion Sensor
Power Cable for RPi
8GB microSD card
Keyboard/Mouse/Monitor
Pimoroni Speaker pHat

# Tools
Solder Iron
Solder
Solder Holder

# Prerequisites
1. Soldering Skills
2. Raspbian OS Setup on a microSD card - https://youtu.be/2Jfv9NO6J2Q

# Step 1 - Hardware Assembly
1. Assemble Pimoroni Speaker pHat and solder - https://learn.pimoroni.com/tutorial/sandyj/assembling-speaker-phat
2. If you are using a Raspberry Pi Zero W, solder all GPIO header pins.

# Step 2 - Install pHat software
1. $ curl -sS https://get.pimoroni.com/speakerphat | bash
2. Hit 'y' twice and reboot when prompted. (Yes, you want the full install.)
[More info about Pimoroni SpeakerpHat here - https://github.com/pimoroni/speaker-phat ]
3. $ cd Pimoroni/speakerphat/test/test.mp3 - Test VLC music
If sound plays, you can move onto the next step. If not, $ sudo apt-get install vlc
4. $ sudo pip install python-vlc
5. $ git clone https://github.com/carolinedunn/Handwashing_Timer_Music 
6. $ cd Handwashing_Timer_Music

