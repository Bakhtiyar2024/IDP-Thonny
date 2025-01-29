from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor

left_sensor = Pin( 10, Pin.IN) #Sensor pins
right_sensor = Pin(11 , Pin.IN)

Motor = Motor()

#last_left_time = tick_ms() #Angle correction variables
#last_right_time = tick_ms()



while True:
    left_value = left_sensor.value()
    right_value = right_sensor.value()
    
    if left_value == 1 and right_value == 1: #Both sensors detect line
       # current_time = tick_ms()
      #  if (last_left_time - last_right_time) > 100:
            # Left sensor detected line more recently so a small right turn
       # elif (last_right_time - last_left_time) > 100:
            # Right sensor detected line more recently so a small left turn
        # else:
        Motor.Forward() #Can move forward once aligned
        
    elif left_value == 0 and right_value == 1:
        print("Adjust Left")
        adjust(timer, turn=left)
    elif left_value == 1 and right_value == 0:
        print("Adjust Right")
        adjust(timer, turn=right)
    sleep(0.1)
        
        
def adjust(timer, turn): #takes in how long we have been on white line, calculates a reduced speed to send to one of the motors
    while left_sensor.value() != 1 or right_sensor.value() != 1:
        Motor.adjust_direction(speed = 75, turn)