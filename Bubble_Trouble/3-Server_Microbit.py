from microbit import *
import radio

#Default is single player
players='1'


radio.on()
display.on()


display.show("1 or 2 Players?",delay=400,wait=True,loop=False,clear=False)

#Initial Number of players configuration
select=False
while(select==False):
    if(button_a.was_pressed()):
        players='1'
        display.show(players,delay=400,wait=False,loop=False,clear=False)
    if(button_b.was_pressed()):
        players='2'
        display.show(players,delay=400,wait=False,loop=False,clear=False)
    if(button_b.is_pressed() and button_a.is_pressed()):
        display.show(players,delay=400,wait=False,loop=False,clear=True)
        select=True

display.show("GO!")    

#Transmit messages from each controller to PC.
while True:
    try:
        incoming=radio.receive()
        if not incoming is None:
            if(players=='1'):
                if(incoming=='A1'):
                    print("p1r ")
                elif(incoming=='A2'):
                    print("p1l ")
                elif(incoming=='A3'):
                    print("p1fire ")
                elif(incoming=='A0'):
                    print("p1nothing ")
            elif(players=='2'):
                if(incoming=='A1'):
                    print("p1r ")
                if(incoming=='B1'):
                    print("p2r ")
                if(incoming=='B2'):
                    print("p2l ")
                if(incoming=='A2'):
                    print("p1l ")
                if(incoming=='B3'):
                    print("p2fire ")
                if(incoming=='A3'):
                    print("p1fire ") 
                if(incoming=='B0'):
                    print("p2nothing ")
                if(incoming=='A0'):
                    print("p1nothing ")   
    except:
        pass
 
       
        