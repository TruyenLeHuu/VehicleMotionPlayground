from carla_vehicle import CarlaVehicle
import rospy
def main():
    """
    Main function
    """
    ego_vehicle = CarlaVehicle()

    try:
        ego_vehicle.run()
    finally:
        if ego_vehicle is not None:
            ego_vehicle.destroy()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
