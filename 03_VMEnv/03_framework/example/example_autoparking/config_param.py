
import time
import random
import rospy
import carla
from carla_msgs.msg import CarlaWorldInfo
import numpy as np
import random
class ParkingConfiguration():
        def __init__(self):
            self.MOVING_POSE_TYPE = 2
            self.PARKING_POSE_TYPE = 3

            #self.UPPER_LIMIT_Y = 3.5
            #self.BUTTON_LIMIT_Y = 0.0
            #self.PARKING_CENTRAL_X = 0.0
            #self.PARKING_THROTTLE = 0.3
            #self.MAX_STEERING = 0.5

            self.UPPER_LIMIT_Y = 3.5
            self.BUTTON_LIMIT_Y = -1.5
            self.PARKING_CENTRAL_X = 0.0
            self.PARKING_THROTTLE = 0.3
            self.MAX_STEERING = 0.5

            
            if self.PARKING_POSE_TYPE == 1 or self.PARKING_POSE_TYPE == 3:
                self.LEVEL1_STEERING = 0.45
                self.LEVEL2_STEERING = 0.35    
                self.LEVEL3_STEERING = 0.1
            
            elif self.PARKING_POSE_TYPE == 2 :
                self.LEVEL1_STEERING = -0.45
                self.LEVEL2_STEERING = -0.35
                self.LEVEL3_STEERING = -0.1


            else:
                pass

            self.INIT_PARKING_POINT = np.random.uniform(5.0, 5.1,1)
            self.X_TURNING_CORNER_1 = 17.0
            self.Y_TURNING_CORNER_1 = -7.0
            self.HEADING_TURNING_CORNER_1 = 270.0

            self.X_TURNING_CORNER_2 = 10.0
            self.Y_TURNING_CORNER_2 = -16.0
            self.HEADING_TURNING_CORNER_2 = 360.0

            self.X_TURNING_CORNER_3 = 14.0
            self.Y_TURNING_CORNER_3 = -15.0
            self.HEADING_TURNING_CORNER_3 = 270.0

class ParkingScenario():
        def __init__(self):

            self.parking_first_point = 0.0
            self.x_FromVehicle_ToParkingOrientation = 3.0
            self.y_FromVehicle_ToParkingOrientation = -4.0
            self.yaw_FromVehicle_ToParkingOrientation = 180.00

            self.x_test = 12.0
            self.y_test = -24.0

            self.parked_locations = [
                carla.Transform(carla.Location(x= self.parking_first_point, y=-4, z=0.05), carla.Rotation(yaw=90)),
                carla.Transform(carla.Location(x= self.parking_first_point + 6, y=-4, z=0.05), carla.Rotation(yaw=90))
                ]
            self.target_location = [
                carla.Transform(carla.Location(x=self.parking_first_point + 3 , y=-4, z=0.05), carla.Rotation(yaw=90))]

            self.vehicle_init_position  = [
                carla.Transform(carla.Location(x=self.parking_first_point - 15.0, y=0, z=0.05), carla.Rotation(yaw=0))]

            self.vehicle_target_position  = [
                carla.Transform(carla.Location(x = self.parking_first_point - 2, y=0, z=0.05), carla.Rotation(yaw=180))]

class ParkingScenario2():
        def __init__(self):
            self.second = 60
            self.minute = 3600
            self.parked_position = [
            {
                "x": -20.3,
                "y": -9.8,
            }
            ,{
                "x": -25.8 - 2.75,
                "y": -9.8,
            }
            ,{
                "x": -20.3+2.75*2,
                "y": 7,
            }]
            self.park_position = [
            # Parking slot line 1
            {
                "x": -20.3,
                "y": 7,
            },
            {
                "x": -20.3 - 2.75,
                "y": 7,
            },
            {
                "x": -20.3 - 2.75*2,
                "y": 7,
            },
            {
                "x": -20.3 - 2.75*3,
                "y": 7,
            },
            {
                "x": -20.3 - 2.75*4,
                "y": 7,
            },
            {
                "x": -20.3 - 2.75*5,
                "y": 7,
            },
            # Parking slot line 2
            {
                "x": -20.3 + 2.75*2,
                "y": 0.5,
            },{
                "x": -20.3 + 2.75,
                "y": 0.5,
            },{
                "x": -20.3 - 2.75,
                "y": 0.5,
            },{
                "x": -25.8,
                "y": 0.5,
            },{
                "x": -25.8 - 2.75,
                "y": 0.5,
            },{
                "x": -25.8 - 2.75*2,
                "y": 0.5,
            },{
                "x": -25.8 - 2.75*3,
                "y": 0.5,
            },{
                "x": -25.8 - 2.75*4,
                "y": 0.5,
            },{
                "x": -25.8 - 2.75*5,
                "y": 0.5,
            },
            # Parking slot line 3
            {
                "x": -20.3 + 2.75*2,
                "y": -10,
            }
            ,{
                "x": -20.3 + 2.75,
                "y": -10,
            }
            ,{
                "x": -20.3 - 2.75,
                "y": -10,
            }
            ,{
                "x": -25.8,
                "y": -10,
            },{
                "x": -25.8 - 2.75*2,
                "y": -10,
            },{
                "x": -25.8 - 2.75*3,
                "y": -10,
            },
            # Parking slot line 4
            {
                "x": -14.8 - 2.75,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*2,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*3,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*4,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*6,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*7,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*8,
                "y": -15.9,
            },{
                "x": -14.8 - 2.75*9,
                "y": -15.9,
            },
            # Parking slot line 5
            {
                "x": -14.8,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75*2,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75*3,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75*7,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75*8,
                "y": -25.9,
            },{
                "x": -14.8 - 2.75*9,
                "y": -25.9,
            },
            # Parking slot line 6
            {
                "x": -14.8 - 2.75*2,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*3,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*4,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*5,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*6,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*7,
                "y": -32.3,
            },{
                "x": -14.8 - 2.75*9,
                "y": -32.3,
            }
            ]
            self.dest_position_4 = {
                "x": -25.8-2.75*2,
                "y": 7,
            }
            self.dest_position_5 = {
                "x": -25.8-2.75*3,
                "y": 7,
            }
            self.parking_first_point = 0.0
            self.x_FromVehicle_ToParkingOrientation = 3.0
            self.y_FromVehicle_ToParkingOrientation = -4.0
            self.yaw_FromVehicle_ToParkingOrientation = 180.00

            self.x_test = 12.0
            self.y_test = -24.0