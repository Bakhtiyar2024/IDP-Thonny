from Infrared_distance_final import get_distance
from QRCode_Reader import QRCodeReader
from MOTOR import Motor
from Linefollowing import LineFollowing
import time
import LinearActuatorSetup

# Initialize Components
motor = Motor()
qr_reader = QRCodeReader()
line_following = LineFollowing()



def box_pickup():
    
    
    while get_distance() > 260:
        motor.Reverse()
        time.sleep(0.1)        
    
    LinearActuatorSetup()
    #line_following.Rev_Follow_line2(265) # will reverse until a distance from the box, doing line following and adjusting
    motor.off()
    time.sleep(5)

    # Try reading QR code
    qr_code = None
    
    while not qr_code:
        qr_code = qr_reader.read_qr_code()
        if qr_code:
            continue
        else:
            time.sleep(0.5)  #retries
            
    motor.Reverse(0.1)
    time.sleep(1)
    motor.off()
            
    motor.Reverse()
    while get_distance() > 15:
        time.sleep(0.1)        
    motor.off()
    
    # Activate linear actuator to lift the box
    motor.Actuator_up(speed = 100)  # Adjust duration as needed
    print("Box lifted. Moving back...")

    motor.Forward(speed = 50)
    time.sleep(2)
    
    # Reverse slowly until a T-junction is detected
    while not (line_following.junction1.value() or line_following.junction2.value()):
        motor.Forward(speed = 30)
        time.sleep(0.1)
    
    motor.off()
    print("T-Junction detected. Box pickup sequence complete!")
    
        
    #Next destination is returned
    next_destination = qr_code
    return next_destination


box_pickup()

    
    
    
    
    

