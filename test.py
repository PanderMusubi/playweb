#!/usr/bin/env python3

from pygame import mixer, time
from time import sleep

mixer.pre_init(44100, -16, 2, 1024)
mixer.init()

#mixer.music.load('sounds/gogo.wav')
#mixer.music.play()
#while mixer.music.get_busy(): 
#    time.Clock().tick(10)

#mixer.Sound('sounds/gogo.wav').play()
#while mixer.get_busy(): 
#    time.Clock().tick(10)

#print(mixer.get_num_channels())
# default 8 channels are available

sound = mixer.Sound('sounds/gogo.wav')
length = sound.get_length()
channel = sound.play()
sleep(length)
#while channel.get_busy(): 
#    time.Clock().tick(10)
