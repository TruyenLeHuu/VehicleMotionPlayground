class HHC_StateMachine():
    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """

        self.State = 'State_Standby'
        self.SsmReq = 'SSMReq_None'
        self.HHCTriggerDeactivate = False
        self.Deactive_Finished = False
        self.HHCTriggerHold = False

    def _hhc_statemachine(self,in_HHCTriggerHold,in_HHCTriggerDeactivate,in_SSMActive):
        
        self.HHCTriggerDeactivate = in_HHCTriggerDeactivate
        self.Deactive_Finished = not in_SSMActive
        self.HHCTriggerHold = in_HHCTriggerHold

        if self.State == 'State_Hold':
            if self.HHCTriggerDeactivate:
                self.State = 'State_Deactivated'
            else:
                self.SsmReq = 'SSMReq_Hold'

        elif self.State == 'State_Deactivated':
            if self.Deactive_Finished:
                self.State = 'State_Standby'
            else:
                self.SsmReq = 'SSMReq_Release'

        elif self.State == 'State_Standby':
            if self.HHCTriggerHold:
                self.State = 'State_Hold'
            else:
                self.SsmReq = 'SSMReq_None'
        else:
            self.State = 'State_Standby'
            
        return self.State, self.SsmReq