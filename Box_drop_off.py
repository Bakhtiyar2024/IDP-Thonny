from Infrared_distance_final import get_distance
from LinearActuator import move_actuator
from MOTOR import Motor
from Linefollowing import LineFollowing
import time
import Location_Routes

# Initialize Components
motor = Motor()
line_following = LineFollowing()

def box_drop_off(destination):
    
    #creating a global variable to keep count of deliveries
    if not hasattr(box_drop_off, "drop_count"):
        box_drop_off.drop_count = 0  # Create the attribute the first time

    box_drop_off.drop_count += 1
    print(f"Function called {box_drop_off.drop_count} times")
    print("Starting Box Drop-Off Sequence...")

    # Move forward slowly until a T-junction is detected
    while not (line_following.junction1.value() or line_following.junction2.value()):
        motor.Forward(speed=20)
        time.sleep(0.1)  # Smooth movement

    motor.off()
    print("T-Junction detected. Lowering the box...")

    # Activate linear actuator to lower the box
    motor.Actuator_down(speed = 50) # Adjust duration as needed
    print("Box dropped off. Moving back...")

     # Reverse slowly until a T-junction is detected
    while not (line_following.junction1.value() or line_following.junction2.value()):
        motor.Reverse(speed = 30)
        time.sleep(0.1)

    motor.off()
    print("Box drop-off sequence complete!")
    
    #fetching next destination
    if box_drop_off.drop_count < 4:
        return "Depot1"
    

# Run the box drop-off sequence
box_drop_off()
