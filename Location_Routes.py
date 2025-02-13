
# Dictionary to store predefined routes
location_routes_from_start = {
    "Depot1" : ["r", "rf"],
    "Depot2" : ["l", "r"]
    
}
location_routes_from_depot_1 = {
    "A": ["l", "s", "rf"],
    "B": ["s", "l", "lf"],
    "C": ["s", "l","s","r","lf"],
    "D": ["s","s","l","lf"]
}

location_routes_to_depot_1 = {
    "A": ["l", "s", "lf"],
    "B": ["r", "r", "lf"],
    "C": ["r", "l","s","r","lf"],
    "D": ["r","r","s","lf"]
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

        