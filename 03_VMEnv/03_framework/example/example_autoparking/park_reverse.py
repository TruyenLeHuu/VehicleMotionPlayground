#!/usr/bin/env python

import time

import rospy
import carla
import json
from carla_msgs.msg import CarlaWorldInfo

import math


from vehicle_control import Vehicle_Control
from config_param import ParkingConfiguration
from config_param import ParkingScenario2
from ros_connect import RosConnect

import pygame

invert_steering_point = -7.8

x_vals = []
y_vals = []


class CarlaVehicle():
    """
    class responsable of:
        -spawning 3 vehicles of which one ego
        -interact with ROS and carla server
        -destroy the created objects
        -execute the parking manoeuvre
    """
    def __init__(self, _vm_api):
        """
        construct object CarlaVehicle with server connection and
        ros node initiation
        """
        self.vm_api = _vm_api
        self.is_parking = 0
        self.state = -1
        
        self.vehicleControl = Vehicle_Control(_vm_api)
        self.parkingParam = ParkingConfiguration()
        self.parkingScenrio = ParkingScenario2()
        self.rosConnect = RosConnect(self)

        self.init_position = {}
        self.tick_number = 0
        self.scenario = 0

        rospy.loginfo('Step 0 - Set up scenarios DONE')
        time.sleep(2)
        
    def waiting_choose_slot_parking(self):
        """
        function to move the ego vehicle into parking slot position
        """
        SCENARIO1_DISTANCE = 4.5

        """ Init position of vehicle when starting park """
        vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()

        if (self.state == 0):

            self.tick_number = 0

            self.init_position = {
            "x": vehicle_lateral,
            "y": vehicle_longitudinal
            }

            """ Send avail parking slots to UI via ros """
            self.rosConnect.publish_parking_slots(self.init_position, self.parkingScenrio.park_position)

            self.state = 1

        """ Waiting for chosen parking slot """
        if (self.state == 1):
            if self.rosConnect.slot == -1 and self.tick_number < 5*self.parkingScenrio.minute:
                
                self.tick_number = self.tick_number + 1
            else:
                if (abs(self.parkingScenrio.park_position[self.rosConnect.slot]["y"] - self.init_position["y"]) < SCENARIO1_DISTANCE):
                    self.scenario = 1
                else:
                    self.scenario = 2
                self.state = 2
                self.tick_number = 0
        if (self.scenario == 1):
            self.move_to_parking_slot_with_states_1()
        elif (self.scenario == 2):
            self.move_to_parking_slot_with_states()
        
    def move_to_parking_slot_with_states_1(self):
        """ Parameters for formula """
        L1 = 4.79                   # Car Length
        L2 = 2.16                   # Car Width
        L3 = 3.04                   # Wheelbase
        D1 = (L1-L3)/2              # @@Car rear to rear axle - not sure
        LG2 = 2.75                  # @@Width of car slot
        STEER_ANGLE_MAX = 32        # 32 degree - 0.56
        # STEER_ANGLE_MAX = 25      # 25 degree - 0.36
        STEER_MAX = 0.56
        ERROR_CALIB = 0.2
        # STEER_MAX = 0.36
        R_MIN = (L3*0.85)/math.sin(math.radians(STEER_ANGLE_MAX))         #@@ Radious min
        R_O22 = math.sqrt(D1**2 + (R_MIN - L2/2)**2)              # Radious of second circle
        H0 = math.sqrt(R_O22**2 - (R_MIN - LG2/2)**2)             #@@

        Y2 = L2/2
        X2 = math.sqrt(4*(R_MIN**2) - (Y2 + R_MIN + H0))
        """ 
        Start moving to slot 
        """
        """ Move to first point near to the slot """
        vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
        if (self.state == 2):
            if abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"]) >  (X2 - R_MIN + ERROR_CALIB) and self.tick_number < self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                if (vehicle_lateral < self.parkingScenrio.park_position[self.rosConnect.slot]["x"]):
                    if heading_angle > 90:
                        self.steer_caculated = 0.05
                    else:
                        self.steer_caculated = -0.05
                    self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=False)
                else:
                    if heading_angle > 90:
                        self.steer_caculated = -0.05
                    else:
                        self.steer_caculated = 0.05
                    self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=True)
                print("vehicle", vehicle_longitudinal,vehicle_lateral)
            else: 
                self.state = 3
        # self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, False)
        # time.sleep(1) 
        """ The same as above """
        if (self.state == 3):
            if abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"]) < (X2 - R_MIN + ERROR_CALIB + ERROR_CALIB) and self.tick_number < 2*self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                if heading_angle > 90:
                    self.steer_caculated = 0.05
                else:
                    self.steer_caculated = -0.05
                self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=False)
                print("vehicle", vehicle_longitudinal, vehicle_lateral)
            else: 
                self.state = 4
        # self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, False)
        # time.sleep(1) 
        """ Act first circle move """
        if (self.state == 4):
            if vehicle_lateral > (self.parkingScenrio.park_position[self.rosConnect.slot]["x"] - (X2/2 - (X2 - R_MIN + ERROR_CALIB))) and self.tick_number < 3*self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                if (self.init_position["y"] > self.parkingScenrio.park_position[self.rosConnect.slot]["y"]):
                    self.vm_api.publish_vehicle_control(0.3, -STEER_MAX, 0.0, reverse=True)
                else: 
                    self.vm_api.publish_vehicle_control(0.3, STEER_MAX, 0.0, reverse=True)
                print("heading_angle", heading_angle)
            else: 
                self.state = 5
        # self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, False)
        # time.sleep(1) 
        """ Act second circle move """
        if (self.state == 5):
            if (self.init_position["y"] > self.parkingScenrio.park_position[self.rosConnect.slot]["y"]):
                if heading_angle < 180 and vehicle_longitudinal > self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 4*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("heading_angle", heading_angle)
                    self.vm_api.publish_vehicle_control(0.1, STEER_MAX, 0.0, reverse=False)
                else:
                    self.state = 6
            else:
                if heading_angle < 180 and vehicle_longitudinal < self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 4*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("heading_angle", heading_angle)
                    self.vm_api.publish_vehicle_control(0.1, -STEER_MAX, 0.0, reverse=False)
                else:
                    self.state = 6
        # self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, False)
        # time.sleep(1)
        """ Last action to reverse vehicle into parking slot"""
        if (self.state == 6):
            if (self.init_position["y"] > self.parkingScenrio.park_position[self.rosConnect.slot]["y"]):
                if vehicle_longitudinal > self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 5*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("vehicle", vehicle_longitudinal,vehicle_lateral)
                    if heading_angle > 180:
                        self.steer_caculated = -0.05
                    else:
                        self.steer_caculated = 0.05
                    self.vm_api.publish_vehicle_control(0.1, self.steer_caculated, 0.0, reverse=False)
                else:
                    self.state = 7
                    self.tick_number = 0
            else: 
                if vehicle_longitudinal < self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 5*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("vehicle", vehicle_longitudinal,vehicle_lateral)
                    if heading_angle < 180:
                        self.steer_caculated = -0.05
                    else:
                        self.steer_caculated = 0.05
                    self.vm_api.publish_vehicle_control(0.1, self.steer_caculated, 0.0, reverse=False)
                else:
                    self.state = 7
                    self.tick_number = 0

        """ Stop vehicle """
        if (self.state == 7):
            if (self.tick_number > 0.25*self.parkingScenrio.second):
                self.state = -1
                self.is_parking = 0
                self.scenario = 0
                """ Log parameter """
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                print("Parameter: ", R_O22, H0, Y2, X2)
                print("Init position: ", self.init_position)
                print("Dest position: ",self.parkingScenrio.park_position[self.rosConnect.slot])
                print("Real dest position: ", vehicle_longitudinal, vehicle_lateral, heading_angle)
                self.rosConnect.publish_done_parking_msg()
            else:
                self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, reverse=False)
                self._brake = 1
                self.tick_number = self.tick_number + 1 

    def move_to_parking_slot_with_states(self):
        """
        function to move the ego vehicle into parking slot position
        """

        """ 
        Start moving to slot 
        """
        """ Move to first point near to the slot """
        vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
        if (self.state == 2):
            if abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"]) > (abs(vehicle_longitudinal - self.parkingScenrio.park_position[self.rosConnect.slot]["y"])) and self.tick_number < 1*self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                # print("heading_angle", heading_angle)
                
                if (vehicle_lateral < self.parkingScenrio.park_position[self.rosConnect.slot]["x"]):
                    if heading_angle > 90:
                        self.steer_caculated = 0.05
                    else:
                        self.steer_caculated = -0.05
                    self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=False)
                else:
                    if heading_angle > 90:
                        self.steer_caculated = -0.05
                    else:
                        self.steer_caculated = 0.05
                    self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=True)
            else:
                self.state = 3
        """ The same as above """
        if (self.state == 3):
            if abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"]) < (abs(vehicle_longitudinal - self.parkingScenrio.park_position[self.rosConnect.slot]["y"])) and self.tick_number < 2*self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                # print("heading_angle", heading_angle)
                if heading_angle > 90:
                    self.steer_caculated = 0.05
                else:
                    self.steer_caculated = -0.05
                self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=False)
            else: 
                self.state = 4
        """ Caculate Arkerman steering angle """
        if (self.state == 4):
            vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
            # self.steer_caculated = math.atan(3.04/(abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"])*0.72))/math.radians(70)
            self.steer_caculated = math.asin(3.04/(abs(vehicle_lateral - self.parkingScenrio.park_position[self.rosConnect.slot]["x"])*0.85))/math.radians(70)
            steer_caculated_print = self.steer_caculated
            self.state = 5
        
        """ Perform reverse the vehicle to parking slot with Arkerman angle """
        if (self.state == 5 and not self.steer_caculated == None):
            if abs(heading_angle) < 180 and self.tick_number < 3*self.parkingScenrio.minute:
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                self.tick_number = self.tick_number + 1 
                print("heading_angle", heading_angle)
                if (self.init_position["y"] > self.parkingScenrio.park_position[self.rosConnect.slot]["y"]):
                    self.vm_api.publish_vehicle_control(0.3, self.steer_caculated, 0.0, reverse=True)
                else:
                    self.vm_api.publish_vehicle_control(0.3, -self.steer_caculated, 0.0, reverse=True)
            else:
                self.state = 6

    
        """ Last action to reverse vehicle into parking slot"""     
        if (self.state == 6):
            if (self.init_position["y"] < self.parkingScenrio.park_position[self.rosConnect.slot]["y"]):
                self.vm_api.publish_vehicle_control(0.1, 0, 0.0, reverse=True)
                if vehicle_longitudinal < self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 4*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("vehicle reverse", vehicle_longitudinal,vehicle_lateral)
                    if heading_angle > 180:
                        self.steer_caculated = 0.05
                    else:
                        self.steer_caculated = -0.05
                    self.vm_api.publish_vehicle_control(0.35, self.steer_caculated, 0.0, reverse=True)
                else:
                    self.state = 7
                    self.tick_number = 0
            else:
                if vehicle_longitudinal > self.parkingScenrio.park_position[self.rosConnect.slot]["y"] and self.tick_number < 5*self.parkingScenrio.minute:
                    vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                    self.tick_number = self.tick_number + 1 
                    print("vehicle also reverse", vehicle_longitudinal,vehicle_lateral)
                    if heading_angle > 180:
                        self.steer_caculated = -0.05
                    else:
                        self.steer_caculated = 0.05
                    self.vm_api.publish_vehicle_control(0.35, self.steer_caculated, 0.0, reverse=True)
                else:
                    self.state = 7
                    self.tick_number = 0
                
        """ Stop vehicle """
        if (self.state == 7):
            if (self.tick_number > 0.25*self.parkingScenrio.second):
                self.state = -1
                self.is_parking = 0
                self.scenario = 0
                """ Log parameter """
                vehicle_longitudinal, vehicle_lateral, heading_angle = self.vehicleControl.relativeVehiclePose()
                print("Init position: ", self.init_position)
                print("Dest position: ",self.parkingScenrio.park_position[self.rosConnect.slot])
                print("Steering Angle: ", self.steer_caculated)
                print("Real dest position: ", vehicle_longitudinal, vehicle_lateral, heading_angle)
                self.rosConnect.publish_done_parking_msg()
            else:
                self.vm_api.publish_vehicle_control(0.0, 0.0, 1.0, reverse=False)
                self._brake = 1
                self.tick_number = self.tick_number + 1 

    def run(self):

        """
        main loop
        """
        # wait for ros-bridge to set up CARLA world
        rospy.loginfo("Waiting for CARLA world (topic: /carla/world_info)...")
        try:
            while True:
                if (self.is_parking == 1):
                    self.waiting_choose_slot_parking()        
        except KeyboardInterrupt:
            print("Shutdown")
    def destroy(self):
        self.vehicleControl.destroy()


# ==============================================================================
# -- main() --------------------------------------------------------------------
# ==============================================================================


