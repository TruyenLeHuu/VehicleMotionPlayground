from carla_ros_api import CarlaRosAPI
from _HHC_Statemachine import HHC_StateMachine
from _HoldTimeManager import LDM_HoldTimeManager
from _pWhl2FxVeh import pWhl2FxVeh
from _SsmStatemachine import SsmStatemachine
from _Trigger_Deactive import HHC_Trigger_Hold_to_Deactivate
from _Trigger_Hold import HHC_Trigger_Standby_to_Hold
from _VhcDeactRampTimeTime import vhcDeactRampTimeTime
from _VhcStatemachine import VhcStatemachine

import time
import rospy

def main():
    """
    Main function
    """
    carla_api = CarlaRosAPI()
    _hhc_statemachine = HHC_StateMachine(carla_api)
    _holdtimemanager = LDM_HoldTimeManager(carla_api)
    _pwhl2fxveh = pWhl2FxVeh(carla_api)
    _ssmstatemachine = SsmStatemachine(carla_api)
    _trigger_deactive = HHC_Trigger_Hold_to_Deactivate(carla_api)
    _trigger_hold = HHC_Trigger_Standby_to_Hold(carla_api)
    _vhcdeactramptimetime = vhcDeactRampTimeTime(carla_api)
    _vhcstatemachine = VhcStatemachine(carla_api)

    try:
        while (not carla_api.exit_flag):
            """ Begin application code """

            _holdtimemanager.Hold_Time_Manager()
            _trigger_deactive.Trigger_Deactive()
            _trigger_hold.Trigger_Hold()
            _hhc_statemachine._hhc_statemachine()
            _vhcdeactramptimetime._vhc_deactramptimetime()
            _ssmstatemachine._ssm_vhc()
            _vhcstatemachine._VhcStatemachine()
            _pwhl2fxveh._pWhl2FxVeh()
            
            """ End application code """
    except KeyboardInterrupt:
        print("Shutdown")
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    