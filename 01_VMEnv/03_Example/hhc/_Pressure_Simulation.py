
class Pressure_Simulation():
    def __init__(self):
        
      
        self.BrakePedalApplied = False
        self.Pressure = 0
        self.p_Model_FL = 0
        self.p_Model_FR = 0
        self.p_Model_RL = 0
        self.p_Model_RR = 0
        self.Ramp_Rate = 2
        self.Area = 16.4
        self.pTar = 0.0

    def _Pressure_Simulation(self,PedalApplied,Active,FxTar, Srv):
        

        self.pTar = -( FxTar / self.Area ) * 0.07

        if PedalApplied > 0.3:
            self.BrakePedalApplied = True
        else:
            self.BrakePedalApplied = False

        self.MCPressure = 200 * PedalApplied

        if self.BrakePedalApplied == True and self.pTar < self.MCPressure:
            self.p_Model_FL = self.MCPressure
            self.p_Model_FR = self.MCPressure
            self.p_Model_RL = self.MCPressure
            self.p_Model_RR = self.MCPressure
        elif self.BrakePedalApplied == False and Active and Srv != 0:
            self.p_Model_FL = self._HAL_Service(Srv,self.pTar,self.p_Model_FL)
            self.p_Model_FR = self._HAL_Service(Srv,self.pTar,self.p_Model_FR)
            self.p_Model_RL = self._HAL_Service(Srv,self.pTar,self.p_Model_RL)
            self.p_Model_RR = self._HAL_Service(Srv,self.pTar,self.p_Model_RR)
        else:
           
            if self.pTar != 0:
                self.p_Model_FL = self.pTar
                self.p_Model_FL = max(self.p_Model_FL, self.MCPressure)
                self.p_Model_FR = self.pTar
                self.p_Model_FR = max(self.p_Model_FR, self.MCPressure)
                self.p_Model_RL = self.pTar
                self.p_Model_RL = max(self.p_Model_RL, self.MCPressure)
                self.p_Model_RR = self.pTar
                self.p_Model_RR = max(self.p_Model_RR, self.MCPressure)
            else:
                self.p_Model_FL = self.p_Model_FL - self.Ramp_Rate
                self.p_Model_FL = max(self.p_Model_FL, self.MCPressure)
                self.p_Model_FR = self.p_Model_FL - self.Ramp_Rate
                self.p_Model_FR = max(self.p_Model_FR, self.MCPressure)
                self.p_Model_RL = self.p_Model_FL - self.Ramp_Rate
                self.p_Model_RL = max(self.p_Model_RL, self.MCPressure)
                self.p_Model_RR = self.p_Model_FL - self.Ramp_Rate
                self.p_Model_RR = max(self.p_Model_RR, self.MCPressure)

        print(" p_Model_FL:",  self.p_Model_FL)
        print(" pTar:",  self.pTar)


        return self.BrakePedalApplied, self.p_Model_FL, self.p_Model_FR, self.p_Model_RL, self.p_Model_RR, self.MCPressure

    def _HAL_Service(self, Srv,pTar,p_Model_XX):
        if Srv == 1: #Hold Service
            if p_Model_XX > pTar:
                p_Model_XX -= self.Ramp_Rate
            else:
                p_Model_XX = pTar

        if Srv == 2: #Inc service
            p_Model_XX += self.Ramp_Rate
            p_Model_XX = min(p_Model_XX,pTar)

        if Srv == 3: #Dec service
            p_Model_XX -= self.Ramp_Rate
            p_Model_XX = max(p_Model_XX,pTar)

        return p_Model_XX