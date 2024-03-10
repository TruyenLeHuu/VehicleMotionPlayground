class VhcStatemachine():
    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """

        self.NoServiceRequired = 0
        self.HoldService_DriverControl_LdcOff = 1
        self.vhcActive = False
        self.vhcDeactivate = False
        self.vhcpGradDeact = 0

        self.vhcTrigDeactivate_B = False
        self.vhcTrig2HoldWORollPrev_B = True
        self.vhcTrigStandby_B = False

        self.vhcState = 'VHCState_Standby'
        self.vhcpTar = 0
        self.vhcpThresholdAct = 0
        self.Entry = False
        self.HALServiceRequest = 0
        self.LDMCor_HHC_Srv = 0

        self.pVehAct = 0
        self.pDriverTar = 0

    def _VhcStatemachine(self, in_vhcActive, in_vhcDeactivate, in_vhcpGradDeact, pVehAct, pDriverTar):


        self.vhcActive = in_vhcActive
        self.vhcDeactivate = in_vhcDeactivate
        self.vhcpGradDeact = in_vhcpGradDeact
        
        self.pVehAct = pVehAct          # Get info from carla or CAN
        self.pDriverTar = pDriverTar    # Get info from carla or CAN

        # calculation vhc trigger deactive
        if (self.vhcActive == False) or ((self.vhcActive == True) and (self.vhcDeactivate == True)):
            self.vhcTrigDeactivate_B = True
        else:
            self.vhcTrigDeactivate_B = False

        # calculation vhc trigger hold
        if self.vhcTrigDeactivate_B:
            self.vhcTrig2HoldWORollPrev_B = False
        else:
            self.vhcTrig2HoldWORollPrev_B = True

        # calculation vhc trigger standby
        if self.vhcActive == False:
            # set trigger to true
            self.vhcTrigStandby_B = True
        else:
            # set trigger to false
            self.vhcTrigStandby_B = False

        # vhc statemachine
        if self.vhcState == 'VHCState_Standby':
            self.vhcpTar = 0
            self.vhcpThresholdAct = 0
            self.HALServiceRequest = self.NoServiceRequired

            if self.vhcTrig2HoldWORollPrev_B:
                self.vhcState = 'VHCState_Hold_wo_RollPrev'
                self.Entry = True

        elif self.vhcState == 'VHCState_Hold_wo_RollPrev':

            self.HALServiceRequest = self.HoldService_DriverControl_LdcOff

            if self.Entry:
                # entry
                self.vhcpTar = max(self.vhcpTar, self.pVehAct)

                # only increase is allowed in consideration of leakage requirement
                # vhcpThresholdAct = max(vhcpThresholdAct, vhcpThresholdMax)
                self.vhcpThresholdAct = 30

                # limit vhcpThresholdAct to vhcpMax
                # vhcpThresholdAct = min(vhcpThresholdAct, vhcpMax)

                # Set vhcpTar to max of previous vhcpTar and driver input
                self.vhcpTar = max(self.vhcpTar, self.pDriverTar)

                # limit vhcpTar to actual vhcpThresholdAct
                self.vhcpTar = min(self.vhcpTar, self.vhcpThresholdAct)

                if self.vhcTrigDeactivate_B:
                    self.vhcState = 'VHCState_Deactivation'
                    self.Entry = True
                else:
                    self.Entry = False
            else:
                # only increase is allowed in consideration of leakage requirement
                # vhcpThresholdAct = max(vhcpThresholdAct, vhcpThresholdMax)
                self.vhcpThresholdAct = 30

                # limit vhcpThresholdAct to vhcpMax
                # vhcpThresholdAct = min(vhcpThresholdAct, vhcpMax)

                # Set vhcpTar to max of previous vhcpTar and driver input
                self.vhcpTar = max(self.vhcpTar, self.pDriverTar)

                # limit vhcpTar to actual vhcpThresholdAct
                self.vhcpTar = min(self.vhcpTar, self.vhcpThresholdAct)

                if self.vhcTrigDeactivate_B:
                    self.vhcState = 'VHCState_Deactivation'
                    self.Entry = True
                else:
                    self.Entry = False

        elif self.vhcState == 'VHCState_Deactivation':
                
                self.HALServiceRequest = self.NoServiceRequired

                # calculate pressure ramp
                if self.vhcpGradDeact > 0: # in case of pressure decrease ensure decrease occur
                    self.vhcpTar -= self.vhcpGradDeact * 0.02
                elif self.vhcpGradDeact < 0: # pressure increase is allowed
                    self.vhcpTar -= self.vhcpGradDeact * 0.02

                # limit to non negative values
                self.vhcpTar = max(self.vhcpTar, 0)

                # only increase is allowed in consideration of leakage requirement
                # vhcpThresholdAct = max(vhcpThresholdAct, vhcpThresholdMax)
                self.vhcpThresholdAct = 30

                # limit vhcFxTar to actual vhcFxThreshold 
                self.vhcpTar = min(self.vhcpTar, self.vhcpThresholdAct)

                if self.vhcTrigStandby_B:
                    self.vhcState = 'VHCState_Standby'
                elif self.vhcTrig2HoldWORollPrev_B:
                    self.vhcState = 'VHCState_Hold_wo_RollPrev'
                    self.Entry = True
                else:
                    self.Entry = False
        else:
            self.vhcState = 'VHCState_Standby'
            self.vhcpTar = 0
            self.HALServiceRequest = self.NoServiceRequired

        self.LDMCor_HHC_Srv = self.HALServiceRequest

        return self.vhcpTar, self.vhcState, self.LDMCor_HHC_Srv