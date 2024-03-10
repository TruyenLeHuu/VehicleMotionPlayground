from vehicle_motion_api import VehicleMotionAPI
import time
import rospy
from enum import Enum
import pygame

pygame.init()
    
vm_api = VehicleMotionAPI()

class TorqueRequest(Enum):
    NO_REQUEST = 0
    INCREASE_TORQUE = 1
    DECREASE_TORQUE = 2

class CCO_state (Enum):
    Off = 0
    Active = 1
    Deactive = 2

class Vehicle:
    def __init__(self):
        self.P_torque_parameter = 0.4
        self.engine_torque = 0
        self.vehicle_ax = 0
        self.P_deviation_torque = 0.3
        self.Driver_braking = False 
        self.ax_when_pressing_button = 0
        self.button_pressed = False
        self.CCO_state_machine = CCO_state.Off
        self._torque_request_value_K1 = self.engine_torque
        self._torque_request_value = self.engine_torque
        self._torque_request = TorqueRequest.NO_REQUEST

    def increase_torque(self):
        # Gửi yêu cầu tăng torque
        self._torque_request_value = self._torque_request_value_K1 + self.P_torque_parameter
        self._torque_request = TorqueRequest.INCREASE_TORQUE
        self._torque_request_value_K1 = self._torque_request_value
        

    def decrease_torque(self):
        # Gửi yêu cầu giảm torque
        self._torque_request_value = self._torque_request_value_K1 - self.P_torque_parameter
        self._torque_request = TorqueRequest.DECREASE_TORQUE
        self._torque_request_value_K1 = self._torque_request_value

    def keep_torque(self):
        # keep torque request as engine torque receive from can
        self._torque_request_value
        self._torque_request_value_K1
        self._torque_request = TorqueRequest.NO_REQUEST

    def re_mapping_torque(self):
        self.button_pressed = False
        self.ax_when_pressing_button = 0
        self._torque_request = TorqueRequest.NO_REQUEST
        self._torque_request_value = self.engine_torque
        self._torque_request_value_K1 = self.engine_torque

    def state_processing (self): 
        #check button state 
        if (self.button_pressed == True):
            self.CCO_state_machine = CCO_state.Active
            vm_api.vehicle_control_throttle_switch(0)

        if (self.button_pressed == False):
            self.CCO_state_machine = CCO_state.Off
            vm_api.vehicle_control_throttle_switch(1)


    def keep_ax(self):
        if (self.CCO_state_machine == CCO_state.Active ):
            if float(self.vehicle_ax) < float(self.ax_when_pressing_button):
                self.increase_torque()
            elif float(self.vehicle_ax) > float(self.ax_when_pressing_button):
                self.decrease_torque()
            else:
                self.keep_torque()
        else:
            self.re_mapping_torque()


    def get_torque_request(self):
        return self._torque_request

    def get_torque_request_value(self):
        return self._torque_request_value



def main():
    """
    Main function
    """
    joysticks = {}
    button_status = False
    vehicle = Vehicle()
    Speed_when_pressing_button = 0
    Speed_vehicle = 0
    try:
        while (not vm_api.exit_flag):
            """ Begin application code """
            vehicle.engine_torque = vm_api.get_vehicle_control().throttle
            vehicle.Driver_braking = vm_api.get_vehicle_control().brake

            if (float(vm_api.get_vehicle_velocity())>0.1):
                vehicle.vehicle_ax = vm_api.get_vehicle_velocity()
            else: 
                vehicle.vehicle_ax = 0.0


            for event in pygame.event.get():
                if event.type == pygame.JOYDEVICEADDED:
                    # This event will be generated when the program starts for every
                    # joystick, filling up the list without needing to create them manually.
                    joy = pygame.joystick.Joystick(event.device_index)
                    joysticks[joy.get_instance_id()] = joy
                    print(f"Joystick {joy.get_instance_id()} connencted")
                if event.type == pygame.JOYBUTTONDOWN:
        
                    if event.button == 11:
                        button_status = not button_status
                        vehicle.ax_when_pressing_button = vehicle.vehicle_ax
                        
                
            vehicle.button_pressed = button_status
            vehicle.state_processing()
            vehicle.keep_ax()
            
            torque_request = vehicle.get_torque_request()
            torque_request_value = vehicle.get_torque_request_value()
            vm_api.vehicle_control_throttle(throttle=torque_request_value)

            print(torque_request_value)
            print(vehicle._torque_request_value_K1)
            print(vehicle.CCO_state_machine)
            print(vehicle.button_pressed)
            print(vehicle.vehicle_ax)
            print(vehicle.ax_when_pressing_button)

            """ End application code """
    except KeyboardInterrupt:
        print("Shutting down")
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    