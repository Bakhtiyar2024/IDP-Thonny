from time import sleep
from machine import Pin
import Box_pick_up
import Start_Button

while True:
    if button() == 1:
        box_pickup()
        
    