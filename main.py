from time import sleep
from machine import Pin
from Box_pick_up import box_pickup
from Box_drop_off import box_drop_off
from Start_Button import check_button()
from Navigation2 import navigation
from Location_Routes
from MOTOR import Motor
from Linefollowing import LineFollowing

line_following = LineFollowing()
motor = Motor()

def main():
    while True:
        while check_button() == True:
            motor.Forward()
            sleep(1)
            line_following.Follow_line() # drive until reached first junction
            
            #get to Depot1 first
            destination = location_routes_from_start["Depot1"]
            navigation(path_to_destination)
            
            #repeat four times
            for i in range(4):
                
                #run depot1
                destination = box_pickup()
                navigation(destination)
                destination = box_drop_off(destination)
                navigation(destination)
                
            for j in range(4):
                
                #run depot2
                destination = box_pickup()
                navigation(destination)
                destination = box_drop_off(destination)
                navigation(destination)
                
            #coming back to starting spot
            line_following.Follow_line()
            motor.Forward()
            sleep(1)
            motor.off()
            line_following.turn(direction = "cw", angle = 180)
            
            check_button() = False
            

if __name__ == "__main__":
    main()
