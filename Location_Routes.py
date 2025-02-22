
# Dictionary to store predefined routes based on turns
location_routes_from_start = {
    "Depot1" : ["r", "rf"],
    "Depot2" : ["l", "r"]
    
}
location_routes_from_depot_1 = {
    "A": ["l", "s", "rf"],
    "B": ["fs", "l", "lf"],
    "C": ["fs", "l","s","r","lf"],
    "D": ["fs","s","l","lf"]
}

location_routes_to_depot_1 = {
    "A": ["l", "s", "rf"],
    "B": ["r", "r", "f"],
    "C": ["r", "l","s","r","f"],
    "D": ["r","r","s","f"]
}

location_routes_from_depot_2 = {
    "A": ["r", "l", "lf"],
    "B": ["s", "r", "s", "rf"],
    "C": ["s", "r","l","lf"],
    "D": ["s","s","r","s","rf"]   
}

location_routes_to_depot_2 = {
    "A": ["r", "l", "lf"],
    "B": ["s", "r", "s", "rf"],
    "C": ["s", "r","l","lf"],
    "D": ["s","s","r","s","rf"]   
}

d1location_routes_to_start = {
    "A": ["l", "rf"],
    "B": ["r", "r", "r", "lf"],
    "C": ["r", "l","s","r", "r", "lf"],
    "D": ["r","r","s","r","lf"]   
}
# Function to reverse a route
def reverse_route(route):
    reverse_map = {"l": "r", "r": "l", "s": "s"}
    return [reverse_map[cmd] for cmd in reversed(route)]

        