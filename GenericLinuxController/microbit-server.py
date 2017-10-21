# This program is uploaded via mu to the micro:bit to be used as a wireless 
# game controller server. You can find mu here: https://github.com/mu-editor/mu
# 
# You will need other micro:bit(s) working as wirelles game controller clients, 
# one for each player. See the microbit-client.py file.
#
# See demonstration video for SuperTuxKart: youtube.com/watch?v=YR-1VejseQA
#
# Philippos Papaphilippou - Sat Oct 21 20:08:06 BST 2017 - GPLv2

from microbit import *
import radio

radio.on()

while True:    
    try:
        incoming = radio.receive()
        if not incoming is None:
            uart.write(incoming+"\n") 
    except:
            pass
