from Linefollowing import follow_line
from MOTORworking import Motor
from T_Junction_Detection import check_sensors
import time

motor = Motor()

# Dictionary to store predefined routes
location_routes = {
    "A": ["forward", "right", "left"],
    "B": ["left", "forward", "right"],
    "C": ["right", "right", "forward"],
}

# Function to reverse a route
def reverse_route(route):
    reverse_map = {"left": "right", "right": "left", "forward": "forward"}
    return [reverse_map[cmd] for cmd in reversed(route)]

# Function to execute a route
def execute_route(route, timeout=5000):
    for command in route:
        while True:
            follow_line()
            junction_detected = check_sensors()
            if junction_detected == command:
                if command == "left":
                    motor.left_turn()
                elif command == "right":
                    motor.right_turn()
                break
            
        time.sleep(1)  # Allow movement before next command
        
        
        
        