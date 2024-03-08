#!/usr/bin/env python

import rospy
import json
from std_msgs.msg import String
from carla_msgs.msg import CarlaEgoVehicleControl

class RosConnect():
    def __init__(self, _parent):
        self.parent = _parent
        self.slot = -1
        rospy.Subscriber("chosen_position", String, self.handle_chosen_position)
        rospy.Subscriber("start_parking", String, self.handle_start_parking)
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        self.pub_steer = rospy.Publisher('steering', String, queue_size=10)
        self.pub_brake = rospy.Publisher('brake', String, queue_size=10)
        self.pub_speed = rospy.Publisher('speed', String, queue_size=10)
        self.doneParkingPub = rospy.Publisher('done_parking', String, queue_size=10)
        self.pub_control = rospy.Publisher('/carla/ego_vehicle/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10)
        
    def handle_start_parking(self, message):
        try:
            self.parent.is_parking = 1
            self.parent.state = 0
            print("Start parking")
        except Exception as e:
            print("Error:", str(e))

    def handle_chosen_position(self, message):
        try:
            parse_data = json.loads(message.data)
            topic = parse_data["topic"]
            if (topic == "slot_chosen"):
                self.slot = parse_data["slot"]
            print("Received from server:", parse_data)
        except Exception as e:
            print("Error:", str(e))

    def publish_parking_slots(self, init_position, park_position):
        slots_position = {
            "topic": "slots_position",
            "init_position": init_position,
            "slots": park_position
        }
        slots_position = json.dumps(slots_position)
        rospy.loginfo(slots_position)
        self.pub.publish(slots_position)

    def publish_speed(self, speed):
        self.pub_speed.publish(str(speed))
    
    def publish_brake(self, brake):
        self.pub_brake.publish(str(brake))
    
    def publish_steer(self, steering):
        self.pub_steer.publish(str(steering))

    def publish_done_parking_msg(self):
        rospy.loginfo("Done parking")
        self.doneParkingPub.publish(json.dumps({"topic": "done_parking"}))
        self.slot = -1

