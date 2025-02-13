from time import sleep
from machine import Pin
from Box_pick_up import box_pickup
from Box_drop_off import box_drop_off
#from Start_Button import check_button()
from Navigation2 import navigation
from Location_Routes import location_routes_from_start, reverse_route, location_routes_from_depot_1, location_routes_from_depot_2, location_routes_to_depot_1
from MOTOR import Motor
from Linefollowing import LineFollowing

LF = LineFollowing()
Motor = Motor()

#while True:
 #   LF.Follow_line()




#navigation(location_routes_from_start["Depot1"])
#navigation(["r", "l", "l", "s", "r", "s", "r", "s", "r", "s", "f"])

box_pickup()
#navigation(["l", "s"])
#LF.turn("cw", 180)

"""
while True:
    #navigation(location_routes_from_start["Depot1"])    
    #navigation(location_routes_from_depot_1[box_pickup()])
    box_pickup()
"""



