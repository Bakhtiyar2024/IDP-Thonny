from Infrared_distance_final import get_distance
from QRCode_Reader import QRCodeReader
from MOTOR import Motor
from Linefollowing import LineFollowing
import time

# Initialize Components
motor = Motor()
#qr_reader = QRCodeReader()
line_following = LineFollowing()

def box_pickup():
    print("Starting Box Pickup Sequence...")
    
    # Move forward slowly until distance ~100mm
    while get_distance() > 100:
        motor.Reverse(speed=30)
        time.sleep(0.1)  # Adjust for smooth movement
    
    motor.off()  # Stop the robot
    print("Reached ~100mm. Attempting to read QR code...")
    
    # Try reading QR code
    qr_code = None
    """
    while not qr_code:
        qr_code = qr_reader.read_qr_code()
        if qr_code:
            print(f"QR Code Detected: {qr_code}")
        else:
            print("No QR code detected, retrying...")
            time.sleep(0.5)
    """
    # Move forward slowly until distance ~20mm
    while get_distance() > 20:
        #line_following.Rev_Follow_line()
        motor.Reverse(40)
        time.sleep(0.1)
    
    motor.off()
    print("Reached ~20mm. Activating linear actuator...")
    
    # Activate linear actuator to lift the box
    motor.Actuator_up(speed = 50)  # Adjust duration as needed
    print("Box lifted. Moving back...")

    # Reverse slowly until a T-junction is detected
    while not (line_following.junction1.value() or line_following.junction2.value()):
        motor.Forward(speed = 30)
        time.sleep(0.1)
    
    motor.off()
    print("T-Junction detected. Box pickup sequence complete!")
    
        
    #Next destination is returned
    #next_destination = qr_code
    #return next_destination

# Run the box pickup sequence
motor.Actuator_down(speed = 100,duration = 6 )

#box_pickup()
    #motor.Reverse(50)
    
