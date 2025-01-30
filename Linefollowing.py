from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor

left_sensor = Pin( 10, Pin.IN) #Sensor pins
right_sensor = Pin(11 , Pin.IN)

Motor = Motor()

#last_left_time = tick_ms() #Angle correction variables
#last_right_time = tick_ms()

on_line = False
start_time = 0
end_time = 0
theta = 0

line_width = 30 #in mm
sensor_spacing = 20
forward_velocity = 20 #mm/s

while True:
    left_value = left_sensor.value()
    right_value = right_sensor.value()
    
    if left_value == 1 and right_value == 1: #Both sensors detect line
       
        if on_line = False:
            start_time = time.ticks_ms()
        on_line = True
        
        Motor.Forward() 
        
        
    elif left_value == 1 and right_value == 0: #therefore off to the right of the line
        print("Adjust Left")
        if on_line = True:
            end_time = time.ticks_ms()
        on_line = False
        adjust(end_time - start_time, turn="left")
        
    elif left_value == 0 and right_value == 1:
        print("Adjust Right")
        if on_line = True:
            end_time = time.ticks_ms()
        on_line = False
        adjust(end_time - start_time, turn="right")
        
    sleep(0.1)
        
        
def adjust(timer, turn): #takes in how long we have been on white line, calculates a reduced speed to send to one of the motors
    theta = (line_width - sensor_spacing)/(timer*forward_velocity)
    while (left_sensor.value() and right_sensor.value()) !=1:
        Motor.adjust_direction(theta = 0.1, turn)
        
    entry(theta)
    sleep(0.2)
        

def entry(theta):
    
        