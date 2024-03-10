
class pWhl2FxVeh():
    def __init__(self):
        """
        Construct object CarlaVehicle with server connection and
        ROS node initiation
        """
     
        self.Pi = 3.14
        self.Abrollumfang_VA = 2.1219
        self.l_WheelRadius_FA = self.Abrollumfang_VA/(2*self.Pi)
        self.Cp_FA = 25
        self.frac_cp_R = self.Cp_FA/self.l_WheelRadius_FA

        self.FxWhl_FL = 0
        self.FxWhl_FR = 0
        self.FxWhl_RL = 0
        self.FxWhl_RR = 0

        self.LDMCor_HHC_FxTar = 0
        self.vhcpTar = 0
    def _pWhl2FxVeh(self,in_vhcpTar):
       
        self.vhcpTar = in_vhcpTar 
        
        self.FxWhl_FL = - self.frac_cp_R * self.vhcpTar
        self.FxWhl_FR = - self.frac_cp_R * self.vhcpTar
        self.FxWhl_RL = - self.frac_cp_R * self.vhcpTar
        self.FxWhl_RR = - self.frac_cp_R * self.vhcpTar

        self.LDMCor_HHC_FxTar = self.FxWhl_FL + self.FxWhl_FR + self.FxWhl_RL + self.FxWhl_RR

        return self.LDMCor_HHC_FxTar