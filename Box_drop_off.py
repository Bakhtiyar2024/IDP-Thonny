from Infrared_distance_final import get_distance
from MOTOR import Motor
from Linefollowing import LineFollowing
from time import sleep
import Location_Routes
from LinearActuatorSetup import LinearActuatorSetup


# Initialize Components
motor = Motor()
line_following = LineFollowing()

def box_drop_off():
    """Follows a line, drops off the box, and repositions itself."""

    # Move forward slightly and do a 180-degree turn to clear entrance junction
    line_following.Follow_line2(1, 100)

    # Follow the line until a junction is detected
    line_following.Follow_line(70)

    # Lower the actuator to drop the box
    motor.Actuator_down(speed=100)

    # Move backward for 2 seconds
    motor.Reverse()
    sleep(2)
    motor.off()

    left_value = 0
    right_value = 0

    # Rotate clockwise for 1 second
    motor.cw_spin(50)
    sleep(1)

    # Keep rotating until both sensors detect the line again
    done = False
    while not done:
        left_value = line_following.left_sensor.value()
        right_value = line_following.right_sensor.value()
        
        if left_value == 1 and right_value == 1:
            done = True
            
    motor.off()
   
"""while True:
    motor.Actuator_up(speed = 100)  # Adjust duration as needed

    line_following.Follow_line()
    line_following.turn("cw", 90)
    motor.off()
    box_drop_off()
    sleep(3)"""
