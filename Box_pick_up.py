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
    LF.Follow_line3(260)
    #while get_distance() > 260:
        #motor.Reverse()
        
    sleep(0.1)        
    
    LinearActuatorSetup()
    #line_following.Rev_Follow_line2(265) # will reverse until a distance from the box, doing line following and adjusting
    motor.off()

    # Try reading QR code
    qr_code = None
    
    while not qr_code:
        qr_code = qr_reader.read_qr_code()
        if qr_code:
            continue
        else:
            sleep(0.5)  #retries
            
    motor.Forward(0.1)
    sleep(1)
    motor.off()
            
 
    LF.Follow_line3(5)

    #while get_distance() > 10:
     #   time.sleep(0.1)
    sleep(0.1)
    motor.off()
    
    # Activate linear actuator to lift the box
    motor.Actuator_up(speed = 100)  # Adjust duration as needed
    #print("Box lifted. Moving back...")
    
    
    
    motor.off()
    motor.Reverse(50)
    sleep(0.65*n)
    motor.off()
    
    left_value = 0
    right_value = 0
    
    motor.cw_spin(50)
    sleep(0.5)
    
    
    done = False
    while done ==False:
        left_value = LF.left_sensor.value()
        right_value = LF.right_sensor.value()
        
        if left_value == 1 or right_value == 1: #Both sensors detect line
            sleep(0.3)
            done = True
            
    motor.off()
    
        
    #Next destination is returned
    next_destination = qr_code
    return next_destination



    
    
    
    
    

