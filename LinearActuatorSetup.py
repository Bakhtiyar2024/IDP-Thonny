from MOTOR import Motor


def LinearActuatorSetup():
    
    motor = Motor()
    
    motor.Actuator_up(speed = 100)
        
    motor.Actuator_down(speed = 100 , duration = 2.2)
    return

#LinearActuatorSetup()
    
