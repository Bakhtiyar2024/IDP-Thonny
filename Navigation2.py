
 #l = acw 90,  r = cw 90,  s = skip,  scw = 180 spin clockwise,  sacw = 180 spin anticlockwise, f == finished
from time import sleep, ticks_ms
from machine import Pin
from Linefollowing import LineFollowing
from MOTOR import Motor

button = Pin(12, Pin.IN, Pin.PULL_DOWN)

LF = LineFollowing()
Motor = Motor()

#path = ["r", "s", "s", "l", "l", "s", "r", "s", "l", "l", "s", "f"]
path = ["r", "l"]
#O_to_1 = []
#1_to_a = []
#1_to_b = []

def navigation(path):
    """Navigates the robot through a given path of steps."""
    
    completed = False
    
    while not completed:
        for step in path:
            # Follow the line until a junction is reached
            adjust = LF.Follow_line() 
        
            if step == "r":  # Turn right at junction
                LF.turn("cw", 90)
                Motor.Forward()
                LF.Follow_line2(2, 100)

            elif step == "l":  # Turn left at junction
                LF.turn("acw", 90)
                LF.Follow_line2(2, 100)
                Motor.off()
                
            elif step == "scw":  # Make a 180-degree clockwise turn
                LF.turn("cw", 180)
                Motor.off()
                completed = True

            elif step == "fs":  # Move forward slightly past junction
                LF.Follow_line2(1, 100)

            elif step == "s":  # Move forward slightly
                LF.Follow_line2(1, 100)

            elif step == "lf":  # Turn left and stop
                LF.turn("acw", 90)
                Motor.off()
                completed = True

            elif step == "rf":  # Turn right and stop
                LF.turn("cw", 90)
                Motor.off()
                completed = True

            elif step == "f":  # Stop navigation
                Motor.off()
                completed = True
                
            
#from Location_Routes import location_routes_from_start, reverse_route, location_routes_from_depot_1, location_routes_from_depot_2

#while True:
 #   navigation(path)
    
#sleep(1)

#LF.Follow_line2(3)
#Motor.Reverse()

#sleep(10)
#LF.turn("cw", 90)


#Motor.off()
#LF.Rev_Follow_line2(100)
    
            
            
            
        
    