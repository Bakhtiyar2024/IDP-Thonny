from MOTOR import Motor
import time


def LinearActuatorSetup():
    
    motor = Motor()
    
    for i in range(2):
        motor.Actuator_up(speed = 100)
        
    start_time = time.time()  # Start time

    motor.Actuator_down(speed = 100 , duration = 2.2)
    return

#LinearActuatorSetup()
    
