
"""
Class for carla
"""

import rospy
from std_msgs.msg import Header, String
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import CameraInfo, NavSatFix, Image, PointCloud2, Imu
from geometry_msgs.msg import Quaternion, Vector3, Pose
from nav_msgs.msg import Odometry
# from derived_object_msgs.msg import ObjectArray
from visualization_msgs.msg import Marker, MarkerArray
from carla_msgs.msg import (CarlaEgoVehicleStatus, CarlaEgoVehicleInfo, CarlaWorldInfo,
                            CarlaActorList, CarlaTrafficLightStatusList,
                            CarlaTrafficLightInfoList, CarlaEgoVehicleControl)


TIMEOUT = 20


class CarlaRosAPI():

    """
    Handles testing of the all nodes
    """
    def __init__(self):
    # Initialize ROS node
        rospy.init_node('nvdia_node', anonymous=True)

        # Create a flag to track whether to exit
        self.exit_flag = False

        # Set up a callback for Ctrl + C
        rospy.on_shutdown(self.shutdown)

    def shutdown(self):
        # Set the exit flag when Ctrl + C is detected
        print("Shutting down")
        self.exit_flag = True
        
    def publish_vehicle_control(self, throttle=0.0, steer=0.0, brake=0.0, hand_brake=False, reverse=False, manual_gear_shift=False, gear=0):

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

    def publish_vehicle_control_manual(self, throttle=0.0, steer=0.0, brake=0.0, hand_brake=False, reverse=False, manual_gear_shift=False, gear=0):

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

    def get_clock(self):
        clock_msg = rospy.wait_for_message("/clock", Clock, timeout=TIMEOUT)
        return clock_msg
    
    def get_vehicle_velocity(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_velocity = msg.velocity
        return vehicle_velocity
    
    def get_vehicle_acceleration(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_acceleration = msg.acceleration
        return vehicle_acceleration
    
    def get_vehicle_orientation(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_orientation = msg.orientation
        return vehicle_orientation
    
    def get_vehicle_rotation(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_rotation = msg.rotation
        return vehicle_rotation
    
    def get_vehicle_location(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_location = msg.location
        return vehicle_location
    
    def get_vehicle_rotation_and_location(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        vehicle_rotation = msg.rotation
        vehicle_location = msg.location
        return vehicle_rotation, vehicle_location
    
    def get_vehicle_location_x_y(self):
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, timeout=TIMEOUT)
        x = msg.location.x
        y = msg.location.y
        return x, y

    def get_vehicle_info(self):
        """
        gets vehicle_info
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/vehicle_info", CarlaEgoVehicleInfo, timeout=TIMEOUT)
        return msg
        self.assertNotEqual(msg.id, 0)
        self.assertEqual(msg.type, "vehicle.tesla.model3")
        self.assertEqual(msg.rolename, "ego_vehicle")
        self.assertEqual(len(msg.wheels), 4)
        self.assertNotEqual(msg.max_rpm, 0.0)
        self.assertNotEqual(msg.moi, 0.0)
        self.assertNotEqual(msg.damping_rate_full_throttle, 0.0)
        self.assertNotEqual(msg.damping_rate_zero_throttle_clutch_engaged, 0.0)
        self.assertNotEqual(
            msg.damping_rate_zero_throttle_clutch_disengaged, 0.0)
        self.assertTrue(msg.use_gear_autobox)
        self.assertNotEqual(msg.gear_switch_time, 0.0)
        self.assertNotEqual(msg.mass, 0.0)
        self.assertNotEqual(msg.clutch_strength, 0.0)
        self.assertNotEqual(msg.drag_coefficient, 0.0)
        self.assertNotEqual(msg.center_of_mass, Vector3())

    def get_odometry(self):
        """
        gets Odometry
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/odometry", Odometry, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "map")
        self.assertEqual(msg.child_frame_id, "ego_vehicle")
        self.assertNotEqual(msg.pose, Pose())

    def get_gnss(self):
        """
        gets Gnss
        """
        msg = rospy.wait_for_message(
            "/carla/ego_vehicle/gnss", NavSatFix, timeout=TIMEOUT)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/gnss")
        self.assertNotEqual(msg.latitude, 0.0)
        self.assertNotEqual(msg.longitude, 0.0)
        self.assertNotEqual(msg.altitude, 0.0)

    def get_imu(self):
        """
        gets IMU sensor node
        """
        msg = rospy.wait_for_message("/carla/ego_vehicle/imu", Imu, timeout=15)
        return msg
        self.assertEqual(msg.header.frame_id, "ego_vehicle/imu")
        self.assertNotEqual(msg.linear_acceleration, 0.0)
        self.assertNotEqual(msg.angular_velocity, 0.0)
        self.assertNotEqual(msg.orientation, 0.0)

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

    # def get_ego_vehicle_objects(self):
    #     """
    #     gets objects node for ego_vehicle
    #     """
    #     msg = rospy.wait_for_message(
    #         "/carla/ego_vehicle/objects", ObjectArray, timeout=15)
    #     return msg
    #     self.assertEqual(msg.header.frame_id, "map")
    #     self.assertEqual(len(msg.objects), 0)

    # def get_objects(self):
    #     """
    #     gets carla objects
    #     """
    #     msg = rospy.wait_for_message("/carla/objects", ObjectArray, timeout=TIMEOUT)
    #     return msg
    #     self.assertEqual(msg.header.frame_id, "map")
    #     self.assertEqual(len(msg.objects), 1)  # only ego vehicle exists

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

