from Infrared_distance_final import get_distance
from LinearActuator import move_actuator
from MOTOR import Motor
from Linefollowing import LineFollowing
import time
import Location_Routes

# Initialize Components
motor = Motor()
line_following2 = LineFollowing()

def box_drop_off(destination):
    
    #creating a global variable to keep count of deliveries
    if not hasattr(box_drop_off, "drop_count"):
        box_drop_off.drop_count = 0  # Create the attribute the first time

    box_drop_off.drop_count += 1

    # Move forward slowly until a T-junction is detected
    motor.Reverse(speed=20)
    while not (line_following.junction1.value() or line_following.junction2.value()):
        time.sleep(0.1)  # Smooth movement

    motor.off()
    print("T-Junction detected. Lowering the box...")

    # Activate linear actuator to lower the box
    motor.Actuator_down(speed = 50) # Adjust duration as needed
    print("Box dropped off. Moving back...")

     # Reverse slowly until a T-junction is detected
    motor.Forward(speed = 30)
    while not (line_following.junction1.value() or line_following.junction2.value()):
        time.sleep(0.1)

    motor.off()
    
    #fetching next destination
    if box_drop_off.drop_count < 4:
        return reverse_route(location_routes_from_depot_A[destination])
    elif box_drop_off.drop_count == 4:
        return reverse_route(location_routes_from_depot_B[destination])
    elif box_drop_off.drop_count == 8:
        reversed_route = reverse_route(location_routes_from_depot_B[destination])
        combined_route = reversed_route.append([r, l])
        return combined_route
    



box_drop_off('A')
