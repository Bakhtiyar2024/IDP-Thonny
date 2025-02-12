
# Dictionary to store predefined routes
location_routes_from_start = {
    "Depot1" : ["r", "l"],
    "Depot2" : ["l", "r"]
    
}
location_routes_from_depot_1 = {
    "A": ["l", "s", "l"],
    "B": ["s", "l", "r"],
    "C": ["s", "l","s","r","r"],
    "D": ["s","s","l","r"]
}

location_routes_from_depot_2 = {
    "A": ["r", "l", "l", "f"],
    "B": ["s", "r", "s", "l"],
    "C": ["s", "r","l","r"],
    "D": ["s","s","r","s","l"]   
}

# Function to reverse a route
def reverse_route(route):
    reverse_map = {"l": "r", "r": "l", "s": "s"}
    return [reverse_map[cmd] for cmd in reversed(route)]

        