
class vhcDeactRampTimeTime():
    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """
        self.SsmReq = 'SSMReq_None'
        self.vhcDeactRampTimeTimeTrig = False
        self.vhcDeactRampTimeTimeTrigK1 = False
        self.vhcpGradDeact = 0
        self.vhcpTar = 0
        
    def _vhc_deactramptimetime(self, in_SsmReq, in_vhcpTar):

        self.vhcDeactRampTimeTimeTrigK1 = self.vhcDeactRampTimeTimeTrig

        self.SsmReq = in_SsmReq
        self.vhcpTar = in_vhcpTar

        if self.SsmReq == 'SSMReq_Release':
            self.vhcDeactRampTimeTimeTrig = True
        else:
            self.vhcDeactRampTimeTimeTrig = False

        # calculation of ramp
        if not self.vhcDeactRampTimeTimeTrig:
            # set default ramp for the ramp coordination
            self.vhcpGradDeact = 0
        elif (self.vhcDeactRampTimeTimeTrig == True and
                self.vhcDeactRampTimeTimeTrigK1 == False):
            # calculation for ramp 1
            # transform to frequency
            self.vhcpGradDeact = (self.vhcpTar - 5) * 4 + 0.0625
            # 5 bar, vehicle start to roll
            # 4 Hz, time ramp parameter in case of deactivation via time ramp
            # 0.0625 offset pressure

        #self.vhcpGradDeact = max (self.vhcpGradDeact, 2)

        print("vhcpGradDeact:", self.vhcpGradDeact)
            
        return self.vhcpGradDeact