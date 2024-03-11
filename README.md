# VehicleMotionPlayground (VMP)

The project contains all the provided code for the VM framework, API, example code, more precisely:
- Folder 01_VMEnv:
    - Contain RosBridge for communication of Carla and application code.
    - Contain code of Client side, that visual the carla on screen and take VM hardware control.
    - Contain example code and template code for application.
- Folder 02_AutoRun:
    - Contain scripts to run all part of framework, included Carla server, Carla client side and Ros bridge.
- Folder 03_Utils:
    - UI, support code for example
    
## Prerequisites environments:
- Ubuntu 20.04 LTS
- Carla 0.9.13
- Ros 1 Noetic

## Getting started:
You must rebuild the ros-bridge source code:

        cd 01_VMEnv/01_RosBridge
        catkin_make

Waiting for build, if error, you must analyze the ROS installed.
After build done:

        source devel/setup.bash
        roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch

It can be error, that is normal.

## How to run:
Run command in terminal: 

        bash 02_AutoRun/run-env.sh

Code application in Template of folder 03_Example and run:

        python3 main.py

## The documentation of Carla simulator API is available in more details here:
[Documentation](https://carla.readthedocs.io/en/latest/python_api/)