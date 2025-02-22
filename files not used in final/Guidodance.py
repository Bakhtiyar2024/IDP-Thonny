from MOTOR import Motor
import time


def guidodance():
    motor = Motor()
    motor.cw_spin()
    
    time.sleep(1)
    
    motor.acw_spin()
    
    time.sleep(1)
    
    for i in range(10):
        motor.Forward()
        time.sleep(0.2)
        motor.Reverse(0.2)
        time.sleep(0.2)
    
    

    
    
    