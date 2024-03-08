from vehicle_motion_api import VehicleMotionAPI
from park_reverse import CarlaVehicle
import time
import rospy

def main():
    """
    Main function
    """
    carla_api = VehicleMotionAPI()
    carla_vehicle = CarlaVehicle(carla_api)
    try:
        while (not carla_api.exit_flag):
            """ Begin application code """
            carla_vehicle.run()
            
            """ End application code """
    except KeyboardInterrupt:
        print("Shutdown")
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    