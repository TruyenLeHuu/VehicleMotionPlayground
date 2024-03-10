class SsmStatemachine():
    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """
        self.TriggerHold = False
        self.TriggerRelease = False
        self.TrigStandby = False

        self.SsmState = 'SSMState_Standby'
        self.vhcActive = False
        self.vhcDeactivate = False
        self.SSMActive = False
        self.LDMCor_HHC_Id = False

        self.SsmReq = 'SSMReq_None'
        self.vhcpTar = 0

    def _ssm_vhc(self,in_SsmReq,in_vhcpTar):

        self.SsmReq = in_SsmReq
        self.vhcpTar = in_vhcpTar

            # Trigger for SSM Phase Hold
        if self.SsmReq == 'SSMReq_Hold':
            self.TriggerHold = True
        else:
            self.TriggerHold = False

        # Trigger for SSM Phase Release
        if self.SsmReq == 'SSMReq_Release':
            self.TriggerRelease = True
        else:
            self.TriggerRelease = False

        # trigger calculation for standby
        if self.vhcpTar <= 0:
            # the trigger is set to true if the requested soll pressure is lower than the master cylinder pressure
            self.TrigStandby = True
        else:
            self.TrigStandby = False

        # switch statement
        if self.SsmState == 'SSMState_Standby':
            # same for ENTRY and STATIC and EXIT

            # set vhc active
            self.vhcActive = False

            # set deactivation flag
            self.vhcDeactivate = False

            # set SSM active
            self.SSMActive = False

            if self.TriggerHold:
                self.SsmState = 'SSMState_HydHold'

        elif self.SsmState == 'SSMState_Release':

            # set vhc active
            self.vhcActive = True

            # set deactivation flag
            self.vhcDeactivate = True

            # set SSM active
            self.SSMActive = True

            if self.TrigStandby:
                self.SsmState = 'SSMState_Standby'
            elif self.TriggerHold:
                self.SsmState = 'SSMState_HydHold'

        elif self.SsmState == 'SSMState_HydHold':

            # set vhc active
            self.vhcActive = True

            # set deactivation flag
            self.vhcDeactivate = False

            # set SSM active
            self.SSMActive = True

            if self.TriggerRelease:
                self.SsmState = 'SSMState_Release'

        else:
            self.SsmState = 'SSMState_Standby'

        if self.SSMActive:
            self.LDMCor_HHC_Id = True
        else:
            self.LDMCor_HHC_Id = False

        return self.SsmState, self.vhcActive, self.vhcDeactivate, self.SSMActive, self.LDMCor_HHC_Id