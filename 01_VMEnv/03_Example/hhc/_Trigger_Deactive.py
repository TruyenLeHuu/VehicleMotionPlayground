class HHC_Trigger_Hold_to_Deactivate():

    def __init__(self):
        """
        construct object CarlaVehicle with server connection and
        ros node initiation
        """
        self.HoldTimeExpired = False
        self.VehicleSpeed = 0
        self.HHCTriggerDeactivate = False
        #self.P_vDeact = P_HHC_vDeact  #vehicle speed threshold < 0,25
        self.P_vDeact = 0.25

        

    def Trigger_Deactive(self, in_VehicleSpeed, in_HoldTimeExpired):

        self.HoldTimeExpired = in_HoldTimeExpired
        #self.VehicleSpeed = self.carla_api.get_vehicle_velocity() #get input from CAN or carla
        self.VehicleSpeed = in_VehicleSpeed

        if (self.HoldTimeExpired == True or                          # hold time expired
            self.VehicleSpeed > self.P_vDeact):                      # vehicle speed higher than vDeact, not standstill

            self.HHCTriggerDeactivate = True
        else:
            self.HHCTriggerDeactivate = False

        #print("HHCTriggerDeactivate:", self.HHCTriggerDeactivate)
        # print("VehicleSpeed:", self.VehicleSpeed)
        # print("In_HoldTimeExpired:", self.HoldTimeExpired)

        return self.HHCTriggerDeactivate
   
        