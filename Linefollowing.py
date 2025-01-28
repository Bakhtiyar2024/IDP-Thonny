from machine import Pin
from time import sleep,tick_ms
from MOTOR import Motor

left_sensor = Pin( 10, Pin.IN) #Sensor pins
right_sensor = Pin(11 , Pin.IN)

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
        print("Turn Left")
        #Motor.left_turn()#Turn left
    elif left_value == 1 and right_value == 0:
        print("Turn Right")
        #Motor.right_turn()#Turn right
    sleep(0.1)
        