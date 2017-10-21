#!/usr/bin/python
"""
Test Bubble Trouble with pywin32
"""
"""
Parses received commands from server micro:bit into appropriate game depended keyboard commands.
In Bubble Trouble, the following keyboard commands are used:

Player 1 right= right control
Player 1 left= left control
Player 1 fire= space 

Player 2 right= character c
Player 2 left= character x
Player 2 fire= character w 

"""
import serial
import time
import pyautogui

#Serial Port Initializations
##Make sure the right COM Port is set as described in instructions
port="COM3"
baud=115200
ser=serial.Serial(port,baud)


#Fill in the control assignments desired using 
#the pyatogui keyboard guide http://pyautogui.readthedocs.io/en/latest/keyboard.html

##################
p1right='right'
p1left='left'
p1fire='space'
p2right='c'
p2left='x'
p2fire='w'
##################

if ser.isOpen():
  print(' '+ser.name+'is open ..')
  #Make sure no button is initially pressed
  pyautogui.keyUp('right')
  pyautogui.keyUp('left')
  pyautogui.keyUp('space')
  pyautogui.keyUp('c')
  pyautogui.keyUp('x')
  pyautogui.keyUp('w')
  
  while(1):
    line="0"
    line=ser.readline()
    #print(line)
    line1=(line.decode().split(" "))[0]
    print("decoded=",line1)
    if(line1=="p1r"):
      pyautogui.keyUp(p1left)
      pyautogui.keyUp(p1fire)
      pyautogui.keyDown(p1right)
    if(line1=="p1l"):
      pyautogui.keyUp(p1right)
      pyautogui.keyUp(p1fire)
      pyautogui.keyDown(p1left)
    if(line1=="p1fire"):
      pyautogui.keyUp(p1right)
      pyautogui.keyUp(p1left)
      pyautogui.keyDown(p1fire)
    if(line1=="p1nothing"):
      pyautogui.keyUp(p1fire)
      pyautogui.keyUp(p1right)
      pyautogui.keyUp(p1left)
    if(line1=="p2r"):
      pyautogui.keyUp(p2left)
      pyautogui.keyUp(p2fire)
      pyautogui.keyDown(p2right)
    if(line1=="p2l"):
      pyautogui.keyUp(p2right)
      pyautogui.keyUp(p2fire)
    if(line1=="p2fire"):
      pyautogui.keyUp(p2left)
      pyautogui.keyUp(p2right)
      pyautogui.keyDown(p2fire)
    if(line1=="p2nothing"):
      pyautogui.keyUp(p2left)
      pyautogui.keyUp(p2right)
      pyautogui.keyUp(p2fire)
    
      
