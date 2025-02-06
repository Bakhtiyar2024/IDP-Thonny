from Linefollowing import follow_line
from MOTORworking import Motor
from T_Junction_Detection import check_sensors
import time


# Dictionary to store predefined routes
location_routes_from_start = {
    "Depot1" : ["r", "l"],
    "Depot2" : ["l", "r"]
    
}
location_routes_from_depot_A = {
    "A": ["l", "s", "l"],
    "B": ["s", "l", "r"],
    "C": ["s", "l","s","r","r"],
    "D": ["s","s","l","r"]
}

location_routes_from_depot_B = {
    "A": ["r", "r"],
    "B": ["s", "r", "s", "l"],
    "C": ["s", "r","l","r"],
    "D": ["s","s","r","s","l"]   
}

# Function to reverse a route
def reverse_route(route):
    reverse_map = {"left": "right", "right": "left", "forward": "forward"}
    return [reverse_map[cmd] for cmd in reversed(route)]

        