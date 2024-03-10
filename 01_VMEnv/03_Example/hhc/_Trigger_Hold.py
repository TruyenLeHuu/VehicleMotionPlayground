
class HHC_Trigger_Standby_to_Hold():
    def __init__(self):
        """
        construct object CarlaVehicle with server connection and
        ros node initiation
        """
        
        self.HHCTriggerDeactivate = False
        self.ax = 0
        self.HHCTriggerHold = False
        #self.P_HHC_SlopeAct = P_HHC_SlopeAct   #parameter 0,4
        self.P_HHC_SlopeAct = 0.4
    def Trigger_Hold(self,in_ax, in_HHCTriggerDeactivate):
    
        self.HHCTriggerDeactivate = in_HHCTriggerDeactivate

        self.ax = in_ax
        # This class calculates the HHC Hold trigger information
        if (self.HHCTriggerDeactivate == False and 
            abs(self.ax) > self.P_HHC_SlopeAct):

            self.HHCTriggerHold = True
        else:
            self.HHCTriggerHold = False

        return self.HHCTriggerHold
    