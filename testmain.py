from time import sleep
from machine import Pin
import Box_pick_up
import Start_Button
from MOTOR import Motor


while True:
    motor = Motor()
    motor.off()
    
    