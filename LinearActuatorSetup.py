from MOTOR import Motor
import time


def LinearActuatorSetup():
    motor = Motor()
    for i in range(5):
        motor.Actuator_up()
        
    start_time = time.time()  # Start time

    for i in range(10):
        motor.Actuator_down()
        print(i+1)

LinearActuatorSetup()
    
