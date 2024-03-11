

"""
Class for carla
"""

import rospy
from std_msgs.msg import Header, String
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import CameraInfo, NavSatFix, Image, PointCloud2, Imu
from geometry_msgs.msg import Quaternion, Vector3, Pose
from nav_msgs.msg import Odometry
from derived_object_msgs.msg import ObjectArray
from visualization_msgs.msg import Marker, MarkerArray
from carla_msgs.msg import (CarlaEgoVehicleStatus, CarlaEgoVehicleInfo, CarlaWorldInfo,
                            CarlaActorList, CarlaTrafficLightStatusList,
                            CarlaTrafficLightInfoList, CarlaEgoVehicleControl)

TIMEOUT = 20

class General():
    def __init__(self):
        self.clock_msg = None
        self.vehicle_velocity = 0.0
        self.vehicle_acceleration = None
        self.vehicle_orientation = None
        self.vehicle_rotation = None
        self.vehicle_location = None
        self.vehicle_controls = None
        self.vehicle_info = None
        self.odometry = None
        self.gnss = None
        self.imu = None
        self.camera_info = None
        self.image = None
        self.dvs_camera_info = None
        self.dvs_image = None
        self.dvs_camera_events = None
        self.lidar = None
        self.semantic_lidar = None
        self.radar = None
        self.ego_vehicle_objects = None
        self.objects = None
        self.marker = None
        self.map = None
        self.world_info = None
        self.actor_list = None
        self.traffic_lights = None
        self.traffic_lights_info = None

    def vehicle_control(self, throttle=0.0, steer=0.0, brake=0.0, hand_brake=False, reverse=False, manual_gear_shift=False, gear=0):

        # Create a publisher for the vehicle control command
        control_pub = rospy.Publisher('/carla/ego_vehicle/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10)

        # Create a message object
        control_msg = CarlaEgoVehicleControl()
        control_msg.throttle = throttle
        control_msg.steer = steer
        control_msg.brake = brake
        control_msg.hand_brake = hand_brake
        control_msg.reverse = reverse
        control_msg.manual_gear_shift = manual_gear_shift
        control_msg.gear = gear
        # Publish the message
        control_pub.publish(control_msg)

    def vehicle_control_throttle(self, throttle=0.0, steer=0.0, brake=0.0, hand_brake=False, reverse=False, manual_gear_shift=False, gear=0):

        # Create a publisher for the vehicle control command
        control_pub = rospy.Publisher('/carla/ego_vehicle/vehicle_control_throttle', CarlaEgoVehicleControl, queue_size=10)

        # Create a message object
        control_msg = CarlaEgoVehicleControl()
        control_msg.throttle = throttle
        control_msg.steer = steer
        control_msg.brake = brake
        control_msg.hand_brake = hand_brake
        control_msg.reverse = reverse
        control_msg.manual_gear_shift = manual_gear_shift
        control_msg.gear = gear
        # Publish the message
        control_pub.publish(control_msg)
    
    def vehicle_control_throttle_switch(self, throttle=0.0, steer=0.0, brake=0.0, hand_brake=False, reverse=False, manual_gear_shift=False, gear=0):

        # Create a publisher for the vehicle control command
        control_pub = rospy.Publisher('/carla/ego_vehicle/vehicle_control_throttle_switch', CarlaEgoVehicleControl, queue_size=10)

        # Create a message object
        control_msg = CarlaEgoVehicleControl()
        # control_msg.throttle = throttle
        control_msg.steer = steer
        control_msg.brake = brake
        control_msg.hand_brake = hand_brake
        control_msg.reverse = reverse
        control_msg.manual_gear_shift = manual_gear_shift
        control_msg.gear = gear
        # Publish the message
        control_pub.publish(control_msg)

    """ Velocity value return:
        1.2 (m/s)
    """
    def get_vehicle_velocity(self):
        return self.vehicle_velocity
    
    """ Acceleration value return:
    {   
        linear: 
            x: 0.0
            y: -0.0
            z: 0.0
        angular: 
            x: 0.0
            y: 0.0
            z: 0.0
    }
    """
    def get_vehicle_acceleration(self):
        return self.vehicle_acceleration
    
    """ Orientation value return:
    {   
        y: -1.6292922383290965e-06
        z: 0.42434795213668
        w: 0.905499207903972
    }
    """
    def get_vehicle_orientation(self):
        return self.vehicle_orientation
    
    """ Rotation value return:
    {   
        roll: -6.103515625e-05
        pitch: 0.00017758490866981447
        yaw: -50.21879577636719
    }
    """
    def get_vehicle_rotation(self):
        return self.vehicle_rotation
    
    """ Location value return:
    {   
        x: 150.9740447998047
        y: -13.36904525756836
        z: 0.040282171219587326
    }
    """
    def get_vehicle_location(self):
        return self.vehicle_location
    
    """ Control value return:
    {   
        header: 
        seq: 0
        stamp: 
            secs: 0
            nsecs:         0
        frame_id: ''
        throttle: 0.0
        steer: 0.0
        brake: 0.0
        hand_brake: False
        reverse: True
        gear: -1
        manual_gear_shift: True 
    }
    """
    def get_vehicle_controls(self):
        return self.vehicle_controls
    
    def get_carla_vehicle_info(self):
        """
        gets vehicle_info
        """
        return self.vehicle_info

    def get_odometry(self):
        """
        gets Odometry
        """
        return self.odometry
    
    """ Gnss value return:
        {   
            latitude: 0.0
            longitude: 0.0
            altitude: 0.0
        }
    """
    def get_gnss(self):
        """
        gets Gnss
        """
        return self.gnss
    
    """ Imu value return:
        {   
            linear_acceleration: 0.0
            angular_velocity: 0.0
            orientation: 0.0
        }
    """
    def get_imu(self):
        """
        gets IMU sensor node
        """
        return self.imu

class RosInterface():
    def __init__(self, general):
        
        self._general = general

        # Initialize ROS node
        rospy.init_node('nvidia_node', anonymous=True)

        self.subcribe_carla_topics()

        # Create a flag to track whether to exit
        self.exit_flag = False

        # Set up a callback for Ctrl + C
        rospy.on_shutdown(self.shutdown)

    def subcribe_carla_topics(self):
        rospy.Subscriber(   "/clock", Clock, self.get_carla_clock)
        rospy.Subscriber(   "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, self.get_carla_vehicle_status)
        rospy.Subscriber(   "/carla/ego_vehicle/vehicle_info", CarlaEgoVehicleInfo, self.get_carla_vehicle_info)
        rospy.Subscriber(   "/carla/ego_vehicle/odometry", Odometry, self.get_carla_odometry)
        rospy.Subscriber(   "/carla/ego_vehicle/gnss", NavSatFix, self.get_vehicle_gnss)
        rospy.Subscriber(   "/carla/ego_vehicle/imu", Imu, self.get_vehicle_imu)

    def get_carla_clock(self, message):
        self._general.clock = message

    def get_carla_vehicle_status(self, msg):
        self._general.vehicle_velocity = msg.velocity
        self._general.vehicle_acceleration = msg.acceleration
        self._general.vehicle_orientation = msg.orientation
        self._general.vehicle_rotation = msg.rotation
        self._general.vehicle_location = msg.location
        self._general.vehicle_controls = msg.control

    def get_carla_vehicle_info(self, msg):
        """
        gets vehicle_info
        """
        self._general.vehicle_info = msg
    
    def get_carla_odometry(self, msg):
        """
        gets Odometry
        """
        self._general.odometry = msg

    def get_vehicle_gnss(self, msg):
        """
        gets Gnss
        """
        self._general.gnss = msg

    def get_vehicle_imu(self, msg):
        """
        gets IMU sensor node
        """
        self._general.imu = msg

    def get_camera_info(self):
        """
        gets camera_info
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/rgb_front/camera_info", CameraInfo, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/rgb_front")
        self.assertEqual(msg.height, 600)
        self.assertEqual(msg.width, 800)

    def get_camera_image(self):
        """
        gets camera_images
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/rgb_front/image", Image, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/rgb_front")
        self.assertEqual(msg.height, 600)
        self.assertEqual(msg.width, 800)
        self.assertEqual(msg.encoding, "bgra8")

    def get_dvs_camera_info(self):
        """
        gets dvs camera info
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/dvs_front/camera_info", CameraInfo, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/dvs_front")
        self.assertEqual(msg.height, 70)
        self.assertEqual(msg.width, 400)

    def get_dvs_camera_image(self):
        """
        gets dvs camera images
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/dvs_front/image", Image, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/dvs_front")
        self.assertEqual(msg.height, 70)
        self.assertEqual(msg.width, 400)
        self.assertEqual(msg.encoding, "bgr8")

    def get_dvs_camera_events(self):
        """
        gets dvs camera events
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/dvs_front/events", PointCloud2, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/dvs_front")

    def get_lidar(self):
        """
        gets Lidar sensor node
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/lidar", PointCloud2, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/lidar")

    def get_semantic_lidar(self):
        """
        gets semantic_lidar sensor node
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/semantic_lidar", PointCloud2, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/semantic_lidar")

    def get_radar(self):
        """
        gets Radar sensor node
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/radar_front", PointCloud2, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/radar_front")

    def get_ego_vehicle_objects(self):
        """
        gets objects node for ego_vehicle
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/objects", ObjectArray, timeout=15)
        return msg
        self.assertEqual(msg.header.frame_id, "map")
        self.assertEqual(len(msg.objects), 0)

    def get_objects(self):
        """
        gets carla objects
        """
        msg = rospy.wait_for_message("/carla/objects", ObjectArray, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "map")
        self.assertEqual(len(msg.objects), 1)  # only ego vehicle exists

    def get_marker(self):
        """
        gets marker
        """
        msg = rospy.wait_for_message("/carla/markers", MarkerArray, timeout=TIMEOUT)
        return msg
        self.assertEqual(len(msg.markers), 1)  # only ego vehicle exists

        ego_marker = msg.markers[0]
        self.assertEqual(ego_marker.header.frame_id, "map")
        self.assertNotEqual(ego_marker.id, 0)
        self.assertEqual(ego_marker.type, 1)
        self.assertNotEqual(ego_marker.pose, Pose())
        self.assertNotEqual(ego_marker.scale, Vector3())
        self.assertEqual(ego_marker.color.r, 0.0)
        self.assertEqual(ego_marker.color.g, 255.0)
        self.assertEqual(ego_marker.color.b, 0.0)

    def get_map(self):
        """
        gets map
        """
        msg = rospy.wait_for_message(
            "/carla/map", String, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(len(msg.data), 0)

    def get_world_info(self):
        """
        gets world_info
        """
        msg = rospy.wait_for_message(
            "/carla/world_info", CarlaWorldInfo, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(len(msg.map_name), 0)
        self.assertNotEqual(len(msg.opendrive), 0)

    def get_actor_list(self):
        """
        gets actor_list
        """
        msg = rospy.wait_for_message(
            "/carla/actor_list", CarlaActorList, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(len(msg.actors), 0)

    def get_traffic_lights(self):
        """
        gets traffic_lights
        """
        msg = rospy.wait_for_message(
            "/carla/traffic_lights/status", CarlaTrafficLightStatusList, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(len(msg.traffic_lights), 0)

    def get_traffic_lights_info(self):
        """
        gets traffic_lights
        """
        msg = rospy.wait_for_message(
            "/carla/traffic_lights/info", CarlaTrafficLightInfoList, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(len(msg.traffic_lights), 0)

    def shutdown(self):
        # Set the exit flag when Ctrl + C is detected
        print("Shutting down")
        self.exit_flag = True

class VehicleMotionAPI():

    def __init__(self):

        self.General = General()

        self.ros_interface = RosInterface(self.General)
    

