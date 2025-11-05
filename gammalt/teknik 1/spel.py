import time
import keyboard
import random
import os

y=1

while True:

    x=random.randrange(0, 4) #ska det skapas ett hinder?
    if x==0:
        xx=random.randrange(0,3) #vilken fil/y-höjd

    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
        if y>0:
            y=y-1

    elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
        if y<2:
            y=y+1


    if y==1:
        print("----------------------------\n\n#\n\n----------------------------\n\n\n\n\n")
    elif y==2:
        print("----------------------------\n\n\n#\n----------------------------\n\n\n\n\n")
    elif y==0:
        print("----------------------------\n#\n\n\n----------------------------\n\n\n\n\n")
    time.sleep(.25)