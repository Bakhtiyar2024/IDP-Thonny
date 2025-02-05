
 #l = acw 90,  r = cw 90,  s = skip,  scw = 180 spin clockwise,  sacw = 180 spin anticlockwise, f == finished

from Linefollowing import LineFollowing
from MOTORworking import Motor

LF = LineFollowing()
Motor = Motor()

path = ["r", "l", "r"]

def navigation(path):
    completed = False
        while completed == False:
        for step in path:
            LF.Follow_line() #will continue until junction is met
        
            if step == "r":
                LF.turn("cw", 90)
                
            elif step == "l":
                LF.turn("acw", 90)
                
            elif step == "s":
                Motor.Forward()
                sleep(0.5) #just so we have passed the junction
                
            elif step == "scw":
                LF.turn("cw", 180)
            
            elif step == "sacw":
                LF.turn("acw", 180)
        
            elif step == "f":
                Motor.off()
                completed = True
                
                
            
            
            
            
            
            
            
            
        
    