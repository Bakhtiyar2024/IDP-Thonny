
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
    completed = False
    while completed == False:
        for step in path:
            adjust = LF.Follow_line() #will continue until junction is met
        
            if step == "r":
                LF.turn("cw", 90)
                Motor.Forward()
                LF.Follow_line2(2, 100)

                
            elif step == "l":
                LF.turn("acw", 90)
                LF.Follow_line2(2, 100)

                Motor.off()
                
            elif step == "scw":
                LF.turn("cw", 180)
                #LF.Follow_line2(1)

                Motor.off()
                completed = True

                
            elif step == "fs":
                LF.Follow_line2(1, 100)
                #LF.Follow_line2(2, 100)
                #Motor.adjust_direction(adjust)
                #sleep(0.5) #just so we have passed the junction
            
            elif step == "s":
                LF.Follow_line2(1, 100)
                #LF.Follow_line2(2, 100)
                #Motor.adjust_direction(adjust)
                #sleep(0.5) #just so we have passed the junction
            
            elif step == "lf":
                LF.turn("acw", 90)
                Motor.off()
                completed = True
                
            elif step == "rf":
                LF.turn("cw", 90)
                Motor.off()
                completed = True
                
            elif step == "f":
                Motor.off()
                completed = True
                #break
                
            
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
    
            
            
            
        
    