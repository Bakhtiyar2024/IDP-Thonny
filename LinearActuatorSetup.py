from MOTOR import Motor


def LinearActuatorSetup():
    """General setup to bring actuator to the correct heght to pick up a box"""
    motor = Motor()
    
    motor.Actuator_up(speed = 100)
        
    motor.Actuator_down(speed = 100 , duration = 2.2)
    return

#LinearActuatorSetup()
    
