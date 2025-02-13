from Infrared_distance_final import get_distance
from MOTOR import Motor
from Linefollowing import LineFollowing
from time import sleep
import Location_Routes
from LinearActuatorSetup import LinearActuatorSetup


# Initialize Components
motor = Motor()
line_following = LineFollowing()

#def box_drop_off(destination):
def box_drop_off():

    """
    #creating a global variable to keep count of deliveries
    if not hasattr(box_drop_off, "drop_count"):
        box_drop_off.drop_count = 0  # Create the attribute the first time

    box_drop_off.drop_count += 1"""
    line_following.Follow_line2(2) #Enter a bit and do a 180 turn so line detectors clear the entrance junction
    line_following.Follow_line()
    LinearActuatorSetup()
    motor.Reverse(50)
    sleep(0.65)
    motor.off()
    left_value = 0
    right_value = 0
    
    motor.cw_spin(50)
    sleep(1)
    
    
    done = False
    while done ==False:
        left_value = line_following.left_sensor.value()
        right_value = line_following.right_sensor.value()
        
        if left_value == 1 and right_value == 1: #Both sensors detect line
            #sleep(0.7)
            done = True
            
    motor.off()
    line_following.Follow_line2(2)

    # Move forward slowly until a T-junction is detected
    #motor.Reverse(speed=40)
    #while not (line_following.junction1.value() and line_following.junction2.value()):
    #    time.sleep(0.1)  # Smooth movement

    motor.off()
   # print("T-Junction detected. Lowering the box...")

    # Activate linear actuator to lower the box
    #motor.Actuator_down(speed = 50) # Adjust duration as needed
    
   # print("Box dropped off. Moving back...")

     # Reverse slowly until a T-junction is detected
    #motor.Forward(speed = 50)
    """line_following.Follow_line2(2)
    motor.Forward(50)
    while not (line_following.junction1.value() or line_following.junction2.value()):
        time.sleep(0.1)"""

    motor.off()
    """
    #fetching next destination
    if box_drop_off.drop_count < 4:
        return reverse_route(location_routes_from_depot_A[destination])
    elif box_drop_off.drop_count == 4:
        return reverse_route(location_routes_from_depot_B[destination])
    elif box_drop_off.drop_count == 8:
        reversed_route = reverse_route(location_routes_from_depot_B[destination])
        combined_route = reversed_route.append([r, l])
        return combined_route
    """



#box_drop_off()
