
class Vehicle_Control():
    def __init__(self, _vm_api):
        """
        construct object CarlaVehicle with server connection and
        ros node initiation
        """
        self.vm_api = _vm_api

    def relativeVehiclePose(self):
        # if parking_pose_type == 2:
        #     vehicle_longitudinal = -(self.parkingScenrio.x_FromVehicle_ToParkingOrientation - self.vehicle.get_location().x)  
        #     vehicle_lateral = self.vehicle.get_location().y - self.parkingScenrio.y_FromVehicle_ToParkingOrientation
        #     vehicle_heading = self.parkingScenrio.yaw_FromVehicle_ToParkingOrientation - self.vehicle.get_transform().rotation.yaw
        vehicle_rotation, vehicle_location = self.vm_api.get_vehicle_rotation_and_location()
        vehicle_longitudinal = vehicle_location.x - 3.0
        vehicle_lateral = vehicle_location.y + 4.0
        vehicle_heading = 180 - vehicle_rotation.yaw
        return vehicle_longitudinal, vehicle_lateral, vehicle_heading
    
        # if control_brake !=0.0:
        #     print("self.vehicle.get_location()  1:",self.vehicle.get_location())
        #     time.sleep(2)
        #     print("self.vehicle.get_location()  2:",self.vehicle.get_location())