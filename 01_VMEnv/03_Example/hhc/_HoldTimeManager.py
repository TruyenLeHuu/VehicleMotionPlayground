class LDM_HoldTimeManager():

    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """
        #DriverBrakeApplied #get input from Carla
        

        self.State = 'State_HoldTimeExpired'
        self.RemainingHoldTime = 0.0       

        self.HoldTimeExpired = False
        self.ActivationRequest = False

        self.DriverBrakeApplied = False
        #self.P_HHC_MaxHoldTime = P_HHC_MaxHoldTime    #parameter 2s
        self.P_HHC_MaxHoldTime = 2.0
        self.P_LDMdT = 0.02

    def Hold_Time_Manager(self,in_DriverBrakeApplied):

        self.DriverBrakeApplied =  in_DriverBrakeApplied               #get input from Carla

        #-----------------------------------------------------------------------------------
        if self.State == 'State_BrakePressed':
            if not self.DriverBrakeApplied:
                self.RemainingHoldTime = self.P_HHC_MaxHoldTime            #parameter 2s
                self.State = 'State_ExtensionPossible'

        elif self.State == 'State_ExtensionPossible':
            if self.RemainingHoldTime > 0.0:
                self.RemainingHoldTime = self.RemainingHoldTime - self.P_LDMdT #C_LDMdT  parameter 0.02
                self.RemainingHoldTime = round (self.RemainingHoldTime,2)
                if self.DriverBrakeApplied:
                    self.State = 'State_BrakePressed'
            else:
                self.State = 'State_HoldTimeExpired'
            self.RemainingHoldTime = max(self.RemainingHoldTime,0.0)

        elif self.State == 'State_HoldTimeExpired':
            
            if self.DriverBrakeApplied:
                self.State = 'State_BrakePressed'
        else:
            self.State = 'State_HoldTimeExpired'
            
        self.HoldTimeExpired = (self.State == 'State_HoldTimeExpired')
        self.ActivationRequest = (self.State == 'State_BrakePressed')

        # print("Current State:", self.State)
        #print("Driver Brake Applied:", self.DriverBrakeApplied)
        # print("HoldTimeExpired:", self.HoldTimeExpired)
        # print("ActivationRequest:", self.ActivationRequest)
        #print("RemainingHoldTime:", self.RemainingHoldTime)
        # print("*****************************************************")
        return self.HoldTimeExpired, self.ActivationRequest, self.State