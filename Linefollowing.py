from machine import Pin
from time import sleep,ticks_ms
from MOTOR import Motor



Motor = Motor()
class LineFollowing:
    
    def __init__(self):
        self.left_sensor = Pin(10, Pin.IN)
        self.right_sensor = Pin(11, Pin.IN)
        self.on_line = False
        self.start_time = 0
        self.end_time = 100
        self.theta = 0

        self.line_width = 25 #in mm
        self.sensor_spacing = 15
        self.forward_velocity = 100 #mm/s
                     


    def adjust(self, timer, turn): #takes in how long we have been on white line, calculates a reduced speed to send to one of the motors
        theta = 1000*(self.line_width - self.sensor_spacing)/(timer*forward_velocity)
        while self.left_sensor.value()!=1 or self.right_sensor.value() !=1:
            Motor.adjust_direction(turn)
            
        #print(theta*180/3.14)
        Motor.damping(theta, turn)
        sleep(0.5)
            
        
    def Follow_line(self):
        while True:
            left_value = self.left_sensor.value()
            right_value = self.right_sensor.value()
            
            if left_value == 1 and right_value == 1: #Both sensors detect line
               
                if self.on_line == False:
                    self.start_time = ticks_ms()
                self.on_line = True
                
                Motor.Forward()
                #print("going forward")
                
                
            elif left_value == 1 and right_value == 0: #therefore off to the right of the line
                #print("Adjust Left")
                if self.on_line == True:
                    self.end_time = ticks_ms()
                self.on_line = False
                
                adjust(end_time - start_time + 1, turn="left")
                
            elif left_value == 0 and right_value == 1:
                #print("Adjust Right")
                if self.on_line == True:
                    self.end_time = ticks_ms()
                self.on_line = False
                adjust(end_time - start_time, turn="right")
                
            sleep(0.1)
            
    def turn(self, direction, angle):#
        done = False
        while done ==False:
            
            if direction == "cw":
                Motor.cw_spin(50)
                sleep(0.005 * angle)
                left_value = self.left_sensor.value()
                right_value = self.right_sensor.value()
                if left_value == 1 or right_value == 1: #Both sensors detect line
                    done = True
            elif direction == "acw":
                Motor.acw_spin(50)
                sleep(0.005 * angle)
                left_value = self.left_sensor.value()
                right_value = self.right_sensor.value()
                if left_value == 1 or right_value == 1: #Both sensors detect line
                    done = True
        Motor.off()
        
        
    
        