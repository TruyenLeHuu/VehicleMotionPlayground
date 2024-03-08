#!/usr/bin/env python

import rospy
import json
from std_msgs.msg import String
from std_msgs.msg import Int32
from carla_msgs.msg import CarlaEgoVehicleControl

class RosConnect():
    def __init__(self, _vehicle_controller):
        self.vehicle_controller = _vehicle_controller
        
        self.slot = -1
        self.sleep_status = 0
        self.sleep_detection_command_brake = 0
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        self.pub_control = rospy.Publisher('/carla/ego_vehicle/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10)
        self.pub_door_status = rospy.Publisher('/carla/ego_vehicle/vehicle_door_status', Int32, queue_size=10)
        self.pub_steer = rospy.Publisher('steering', String, queue_size=10)
        self.pub_brake = rospy.Publisher('brake', String, queue_size=10)
        self.pub_speed = rospy.Publisher('speed', String, queue_size=10)

        rospy.Subscriber("/carla/ego_vehicle/vehicle_control_light", Int32, self.control_light)
        rospy.Subscriber("/carla/ego_vehicle/vehicle_control_door", Int32, self.control_door)

    def publish_status(self):
        self.pub_door_status.publish(self.vehicle_controller.get_door_status())
        
    def vehicle_control_with_ros(self, control_throttle, control_steer, control_brake, 
                                 vehicle_reverse = False, vehicle_handbrake = False, vehicle_mg_shift = False, vehicle_gear = 0):
        control_msg = CarlaEgoVehicleControl()
        control_msg.throttle = control_throttle
        control_msg.steer = control_steer
        control_msg.brake = control_brake
        control_msg.reverse = vehicle_reverse
        control_msg.hand_brake = vehicle_handbrake
        control_msg.manual_gear_shift = vehicle_mg_shift
        control_msg.gear = vehicle_gear
        self.pub_control.publish(control_msg)

    def control_door(self, message):
        try:
            self.vehicle_controller.set_door(message)
        except Exception as e:
            print("Error:", str(e))

    def control_light(self, message):
        try:
            if message.data == 1:
                self.vehicle_controller.set_light_blink()
            else:
                self.vehicle_controller.set_light_not_blink()
        except Exception as e:
            print("Error:", str(e))

    def publish_speed(self, speed):
        self.pub_speed.publish(str(speed))
    
    def publish_brake(self, brake):
        self.pub_brake.publish(str(brake))
    
    def publish_steer(self, steering):
        self.pub_steer.publish(str(steering))

