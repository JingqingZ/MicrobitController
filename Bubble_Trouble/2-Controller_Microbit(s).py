from microbit import *
import radio

#Choose a unique one character player_id
player_id='A'
#default control mode is accelerometer only
mode='1'

#Turn on required coponents
radio.on()
display.on()

#Thresholds can be tuned according to player's comfort.
right_threshold=450
left_threshold=-450
fire_threshold=400

#Initial Control Mode Configuration
display.show("Control Mode 1 or 2?",delay=400,wait=True,loop=False,clear=False)
select=False
while(select==False):
    if(button_a.was_pressed()):
        mode='1'
        display.show(mode,delay=400,wait=False,loop=False,clear=False)
    if(button_b.was_pressed()):
        mode='2'
        display.show(mode,delay=400,wait=False,loop=False,clear=False)
    if(button_b.is_pressed() and button_a.is_pressed()):
        select=True
        display.show(mode,delay=400,wait=False,loop=False,clear=True)

display.show(player_id)


#Each control is designated a distinct state. (0->no movement, 1-> go right, 2-> go left, 3->fire)
old_state='0'
state='0'

while True:
    old_state=state
    x=accelerometer.get_x()
    y=accelerometer.get_y()
  
# Accelerometer controlled
    if(mode=='1'):
        if(x>right_threshold):
            state='1'
        elif(x<-left_threshold):
            state='2'
        elif(y>fire_threshold):
            state='3'
        else:
            state='0'
            
#PushButtons for movement, and accelerometers to fire
    else:
        if(button_b.is_pressed()):
            state='1'
        elif(button_a.is_pressed()):
            state='2'
        elif(y>400):
            state='3'
        else:
            state='0'
    
#only send a radio message upon detecting a change in state to minimize traffic at receiver.    
    if(state!=old_state):
        radio.send(player_id+state)
    
   
