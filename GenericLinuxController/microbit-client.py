# This program is uploaded via mu to the micro:bit to be used as a wireless 
# game controller. You can find mu here: https://github.com/mu-editor/mu
# 
# For multi-player support you can change the id using 'A', 'B', 'C' or 'D'
# for every micro:bit game controller client. You will need another micro:bit
# working as a server. See the microbit-server.py file.
#
# See demonstration video for SuperTuxKart: youtube.com/watch?v=YR-1VejseQA
#
# Philippos Papaphilippou - Sat Oct 21 20:08:06 BST 2017 - GPLv2

from microbit import *
import radio

#compass.calibrate()
radio.on()

id = 'A'

prev_vector = 0,0,0,0,0,0,0,0

while True:

	vector = button_a.is_pressed(), button_b.is_pressed(),\
		accelerometer.get_x()>256, accelerometer.get_x()<-256,\
		accelerometer.get_y()>256, accelerometer.get_y()<-256,\
		pin0.is_touched(), pin1.is_touched(), pin2.is_touched()
	
	if prev_vector!=vector:
		s = ""
		for v in vector:
			if v:
				s+= '1'
			else:
				s+= '0'	
		radio.send(id+s)
	prev_vector = vector
