from Infrared_distance_final import get_distance
from QRCode_Reader import QRCodeReader
from MOTOR import Motor
from Linefollowing import LineFollowing
from time import sleep
from LinearActuatorSetup import LinearActuatorSetup

# Initialize Components
motor = Motor()
qr_reader = QRCodeReader()
LF = LineFollowing()



def box_pickup(n=4):
    """Follows a line, picks up a box, and returns the next destination."""

    # Follow the line until a QR code is detected
    qr_code = LF.Follow_line4()
    
    sleep(0.1)        
    motor.off()
         
    # Continue following the line for 7 units of distance
    LF.Follow_line3(7)

    # Activate the linear actuator to lift the box
    motor.Actuator_up(speed=100)  

    # Move the robot in reverse for a certain duration based on `n` boxes
    motor.Reverse(50)
    sleep(0.68 * n)
    motor.off()
    
    left_value = 0
    right_value = 0

    # Rotate clockwise for 1 second
    motor.cw_spin(50)
    sleep(1)
    
    # Keep rotating until both sensors detect the line again
    done = False
    while not done:
        left_value = LF.left_sensor.value()
        right_value = LF.right_sensor.value()
        
        if left_value == 1 and right_value == 1:
            done = True
            
    motor.off()
        
    # Return the detected QR code as the next destination
    return qr_code


#box_pickup()
    
    
    
    
    

