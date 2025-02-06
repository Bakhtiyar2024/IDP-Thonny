from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor



Motor = Motor()
class LineFollowing:
    
    def __init__(self):
        self.left_sensor = Pin(22, Pin.IN)
        self.right_sensor = Pin(28, Pin.IN)
        self.junction1 = Pin(27, Pin.IN)
        self.junction2 = Pin(26, Pin.IN)
        
        
        

                     


    def adjust(self, turn): #takes in how long we have been on white line, calculates a reduced speed to send to one of the motors
        while self.left_sensor.value()!=1 or self.right_sensor.value() !=1:
            Motor.adjust_direction(turn)
            

            
        
    def Follow_line(self):
        following = True
        while following == True:
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            junction1 = self.junction1.value()
            junction2 = self.junction2.value()

            if (junction1 or junction2) ==1 :
                Motor.off()
                following = False
                
            elif left_value == 0 and right_value == 0:
                sleep(0.01)
                
            elif left_value == 1 and right_value == 1: #Both sensors detect line
               
                Motor.Forward()
                
            elif left_value == 1 and right_value == 0: #therefore off to the right of the line
                
                self.adjust( turn="left")
                
            elif left_value == 0 and right_value == 1:
                
                self.adjust( turn="right")
                
                            
                
        sleep(0.01)
        #break
        
            
    def turn(self, direction, angle):#
        done = False
        while done ==False:
            
            if direction == "cw":
                Motor.cw_spin(50)
                sleep(0.005 * angle)
                
            elif direction == "acw":
                Motor.acw_spin(50)
                sleep(0.005 * angle)
                
            done2 = False
            while done2 == False:
                left_value = self.left_sensor.value()
                right_value = self.right_sensor.value()
                if left_value == 1 or right_value == 1: #Both sensors detect line
                    done2 = True
                sleep(0.01)
                
            done = True
                
        
        Motor.Forward()
        sleep(0.5)
        Motor.off()
        #break