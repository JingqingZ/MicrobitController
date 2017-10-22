# This program is uploaded via mu to the micro:bit to be used as a Neverball
# controller. You can find mu here: https://github.com/mu-editor/mu
# 
# See demonstration videos: 
# https://www.youtube.com/watch?v=hTfFDC1JrFI 
# https://www.youtube.com/watch?v=nzTZKqwdBv8 
#
# Philippos Papaphilippou - Sat Oct 21 20:08:06 BST 2017 - GPLv2

from microbit import *

compass.calibrate()

while True:
    heading = compass.heading() # not used at the moment
    dirx = accelerometer.get_x()
    diry = accelerometer.get_y()
    dirz = accelerometer.get_z() # not used at the moment
    
    uart.write("c%d\nx%d\ny%d\nz%d\n"% (heading, dirx, diry, dirz))    
