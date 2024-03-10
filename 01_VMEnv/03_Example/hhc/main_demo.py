#from carla_ros_api import CarlaRosAPI
from _HHC_Statemachine import HHC_StateMachine
from _HoldTimeManager import LDM_HoldTimeManager
from _pWhl2FxVeh import pWhl2FxVeh
from _SsmStatemachine import SsmStatemachine
from _Trigger_Deactive import HHC_Trigger_Hold_to_Deactivate
from _Trigger_Hold import HHC_Trigger_Standby_to_Hold
from _VhcDeactRampTimeTime import vhcDeactRampTimeTime
from _VhcStatemachine import VhcStatemachine
from _Pressure_Simulation import Pressure_Simulation
from vehicle_motion_api import VehicleMotionAPI
#from  carla_ros_api import CarlaRosAPI
import matplotlib.pyplot as plt
#import carla
import time
#import rospy

def main():
    """
    Main function
    """
    #carla_api = CarlaRosAPI()
    
   

if __name__ == '__main__':
    
    No = 0
    vm_api = VehicleMotionAPI()
    _holdtimemanager = LDM_HoldTimeManager()
    _trigger_deactive = HHC_Trigger_Hold_to_Deactivate()
    _trigger_hold = HHC_Trigger_Standby_to_Hold()
    _hhc_statemachine = HHC_StateMachine()
    _vhcdeactramptimetime = vhcDeactRampTimeTime()
    _ssmstatemachine = SsmStatemachine()
    _vhcstatemachine = VhcStatemachine()
    _pwhl2fxveh = pWhl2FxVeh()
    _pressure_simulation = Pressure_Simulation()
    

    Hold_Time_States = []
    HoldTimeExpireds = []
    HHCTriggerDeactivates = []
    HHCTriggerHolds = []
    HHC_States = []
    SsmReqs = []
    vhcpGradDeacts = []
    SsmStates = []
    vhcActives = []
    vhcDeactivates = []
    SSMActives = []
    LDMCor_HHC_Ids = []
    vhcpTars = []
    vhcStates = []
    LDMCor_HHC_Srvs = []
    LDMCor_HHC_FxTars = []
    p_Model_FLs = []
    p_Model_FRs = []
    p_Model_RLs = []
    p_Model_RRs = []
    MCPressures = []
    pVehActs = []
    pDriverTars = []
    DriverBrakeApplieds = []

    Hold_Time_State = 'State_HoldTimeExpired'
    HoldTimeExpired = False
    HHCTriggerDeactivate = False
    HHCTriggerHold = False
    HHC_State = 'State_Standby'
    SsmReq = 'SSMReq_None'
    vhcpGradDeact = 0
    SsmState = 'SSMState_Standby'
    vhcActive = False
    vhcDeactivate = False
    SSMActive = False
    LDMCor_HHC_Id = False
    vhcpTar = 0
    vhcState = 'VHCState_Standby'
    LDMCor_HHC_Srv = 0
    LDMCor_HHC_FxTar = 0
    PedalApplied = 0
    p_Model_FL = 0
    p_Model_FR = 0
    p_Model_RL = 0
    p_Model_RR = 0
    MCPressure = 0
    pVehAct = 0
    pDriverTar = 0
    DriverBrakeApplied = False

    while (1) :   
        #ax = carla_api.get_vehicle_acceleration() #get input from CAN or carla
        ax = vm_api.get_vehicle_acceleration_x()
        # pitch = vm_api.get_vehicle_acceleration().
        # PedalApplied Carla
        PedalApplied = vm_api.get_vehicle_control().brake

        DriverBrakeApplied,p_Model_FL,p_Model_FR,p_Model_RL,p_Model_RR,MCPressure = _pressure_simulation._Pressure_Simulation(PedalApplied,LDMCor_HHC_Id,LDMCor_HHC_FxTar,LDMCor_HHC_Srv)
        pVehAct = p_Model_FL
        pDriverTar = MCPressure
        HoldTimeExpired, ActivationRequest, Hold_Time_State = _holdtimemanager.Hold_Time_Manager(DriverBrakeApplied)
        HHCTriggerDeactivate = _trigger_deactive.Trigger_Deactive(0,HoldTimeExpired)
        HHCTriggerHold = _trigger_hold.Trigger_Hold(ax, HHCTriggerDeactivate)
        HHC_State, SsmReq = _hhc_statemachine._hhc_statemachine(HHCTriggerHold,HHCTriggerDeactivate,SSMActive)
        vhcpGradDeact = _vhcdeactramptimetime._vhc_deactramptimetime(SsmReq, vhcpTar)
        SsmState, vhcActive, vhcDeactivate, SSMActive, LDMCor_HHC_Id = _ssmstatemachine._ssm_vhc(SsmReq, vhcpTar)
        vhcpTar, vhcState, LDMCor_HHC_Srv = _vhcstatemachine._VhcStatemachine(vhcActive, vhcDeactivate, vhcpGradDeact,pVehAct, pDriverTar)
        LDMCor_HHC_FxTar = _pwhl2fxveh._pWhl2FxVeh(vhcpTar)
        print(PedalApplied)
        print(ax)
        # print(vm_api.get_vehicle_acceleration())
        # print(LDMCor_HHC_FxTar)
        force = {
            "x": (LDMCor_HHC_FxTar*1.2) / 4,
            "y": 0,
            "z": 0
            }
        vm_api.vehicle_add_force(force)


        # print("Current State:", State)
        # print("HoldTimeExpired:", HoldTimeExpired)
        # print("ActivationRequest:", ActivationRequest)
        # print("HHCTriggerDeactivate:", HHCTriggerDeactivate)
        # print("*****************************************************")
        # print("vhcpTar:", vhcpTar)
        # print("p_Model_FL:", p_Model_FL)

        Hold_Time_States.append(Hold_Time_State)
        HoldTimeExpireds.append(int(HoldTimeExpired))
        HHCTriggerDeactivates.append(int(HHCTriggerDeactivate))
        HHCTriggerHolds.append(int(HHCTriggerHold))
        HHC_States.append(HHC_State)
        SsmReqs.append(SsmReq)
        vhcpGradDeacts.append(vhcpGradDeact)
        SsmStates.append(SsmState)
        vhcActives.append(int(vhcActive))
        vhcDeactivates.append(int(vhcDeactivate))
        SSMActives.append(int(SSMActive))
        LDMCor_HHC_Ids.append(int(LDMCor_HHC_Id))
        vhcpTars.append(vhcpTar)
        vhcStates.append(vhcState)
        LDMCor_HHC_Srvs.append(int(LDMCor_HHC_Srv))
        LDMCor_HHC_FxTars.append(LDMCor_HHC_FxTar)
        DriverBrakeApplieds.append(DriverBrakeApplied)
        p_Model_FLs.append(p_Model_FL)
        p_Model_FRs.append(p_Model_FR)
        p_Model_RLs.append(p_Model_RL)
        p_Model_RRs.append(p_Model_RR)
        MCPressures.append(MCPressure)
        pVehActs.append(pVehAct)
        pDriverTars.append(pDriverTar)

# fig, axs = plt.subplots(24)

# # Gán dữ liệu vào mỗi subplot
# axs[0].plot(Hold_Time_States)
# axs[1].plot(HoldTimeExpireds)
# axs[2].plot(HHCTriggerDeactivates)
# axs[3].plot(HHCTriggerHolds)
# axs[4].plot(HHC_States)
# axs[5].plot(SsmReqs)
# axs[6].plot(vhcpGradDeacts)
# axs[7].plot(SsmStates)
# axs[8].plot(vhcActives)
# axs[9].plot(vhcDeactivates)
# axs[10].plot(SSMActives)
# axs[11].plot(LDMCor_HHC_Ids)
# axs[12].plot(vhcpTars)
# axs[13].plot(vhcStates)
# axs[14].plot(LDMCor_HHC_Srvs)
# axs[15].plot(LDMCor_HHC_FxTars)
# axs[16].plot(DriverBrakeApplieds)
# axs[17].plot(p_Model_FLs)
# axs[18].plot(p_Model_FRs)
# axs[19].plot(p_Model_RLs)
# axs[20].plot(p_Model_RRs)
# axs[21].plot(MCPressures)
# axs[22].plot(pVehActs)
# axs[23].plot(pDriverTars)


# # Thêm nhãn vào bên phải và xoay chúng ngang
# axs[0].set_ylabel('Hold_Time_States', rotation=0, ha='left')
# axs[0].yaxis.set_label_coords(1.02, 0.5)
# axs[1].set_ylabel('HoldTimeExpireds', rotation=0, ha='left')
# axs[1].yaxis.set_label_coords(1.02, 0.5)
# axs[2].set_ylabel('HHCTriggerDeactivates', rotation=0, ha='left')
# axs[2].yaxis.set_label_coords(1.02, 0.5)
# axs[3].set_ylabel('HHCTriggerHolds', rotation=0, ha='left')
# axs[3].yaxis.set_label_coords(1.02, 0.5)
# axs[4].set_ylabel('HHC_States', rotation=0, ha='left')
# axs[4].yaxis.set_label_coords(1.02, 0.5)
# axs[5].set_ylabel('SsmReqs', rotation=0, ha='left')
# axs[5].yaxis.set_label_coords(1.02, 0.5)
# axs[6].set_ylabel('vhcpGradDeacts', rotation=0, ha='left')
# axs[6].yaxis.set_label_coords(1.02, 0.5)
# axs[7].set_ylabel('SsmStates', rotation=0, ha='left')
# axs[7].yaxis.set_label_coords(1.02, 0.5)
# axs[8].set_ylabel('vhcActives', rotation=0, ha='left')
# axs[8].yaxis.set_label_coords(1.02, 0.5)
# axs[9].set_ylabel('vhcDeactivates', rotation=0, ha='left')
# axs[9].yaxis.set_label_coords(1.02, 0.5)
# axs[10].set_ylabel('SSMActives', rotation=0, ha='left')
# axs[10].yaxis.set_label_coords(1.02, 0.5)
# axs[11].set_ylabel('LDMCor_HHC_Ids', rotation=0, ha='left')
# axs[11].yaxis.set_label_coords(1.02, 0.5)
# axs[12].set_ylabel('vhcpTars', rotation=0, ha='left')
# axs[12].yaxis.set_label_coords(1.02, 0.5)
# axs[13].set_ylabel('vhcStates', rotation=0, ha='left')
# axs[13].yaxis.set_label_coords(1.02, 0.5)
# axs[14].set_ylabel('LDMCor_HHC_Srvs', rotation=0, ha='left')
# axs[14].yaxis.set_label_coords(1.02, 0.5)
# axs[15].set_ylabel('LDMCor_HHC_FxTars', rotation=0, ha='left')
# axs[15].yaxis.set_label_coords(1.02, 0.5)
# axs[16].set_ylabel('DriverBrakeApplieds', rotation=0, ha='left')
# axs[16].yaxis.set_label_coords(1.02, 0.5)
# axs[17].set_ylabel('p_Model_FLs', rotation=0, ha='left')
# axs[17].yaxis.set_label_coords(1.02, 0.5)
# axs[18].set_ylabel('p_Model_FRs', rotation=0, ha='left')
# axs[18].yaxis.set_label_coords(1.02, 0.5)
# axs[19].set_ylabel('p_Model_RLs', rotation=0, ha='left')
# axs[19].yaxis.set_label_coords(1.02, 0.5)
# axs[20].set_ylabel('p_Model_RRs', rotation=0, ha='left')
# axs[20].yaxis.set_label_coords(1.02, 0.5)
# axs[21].set_ylabel('MCPressures', rotation=0, ha='left')
# axs[21].yaxis.set_label_coords(1.02, 0.5)
# axs[22].set_ylabel('pVehActs', rotation=0, ha='left')
# axs[22].yaxis.set_label_coords(1.02, 0.5)
# axs[23].set_ylabel('pDriverTars', rotation=0, ha='left')
# axs[23].yaxis.set_label_coords(1.02, 0.5)

# plt.show()      
    # try:
    #    main()
    # except rospy.ROSInterruptException:
    #     pass
