from vehicle_motion_api import VehicleMotionAPI
import time
import rospy

def main():
    """
    Main function
    """
    VM = VehicleMotionAPI()
    try:
        while (not VM.ros_interface.exit_flag):
            """ Begin application code """
            print(VM.General.get_imu())
            time.sleep(0.01)
            """ End application code """
    except KeyboardInterrupt:
        print("Shutting down")
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    