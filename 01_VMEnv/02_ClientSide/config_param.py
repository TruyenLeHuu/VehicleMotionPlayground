import carla
import numpy as np

class ParkingScenario():
        def __init__(self):
            self.parking_first_point = 0.0
            self.vehicle_init_position  = [
                carla.Transform(carla.Location(x=self.parking_first_point - 15.0, y=0, z=0.05), carla.Rotation(yaw=0))]