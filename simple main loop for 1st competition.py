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


Motor.Forward()
sleep(2)
navigation(location_routes_from_start["Depot1"])
depot1 = True
boxes_from1 = 0
while depot1 == True:
    next1 = box_pickup(boxes_from1)
    navigation(location_routes_from_depot_1[next1])
    sleep(1)
    box_drop_off()
    navigation(location_routes_to_depot_1[next1])
    boxes_from1 += 1
    if boxes_from1 > 3:
        depot1 = False
        
Motor.off()
        
    
