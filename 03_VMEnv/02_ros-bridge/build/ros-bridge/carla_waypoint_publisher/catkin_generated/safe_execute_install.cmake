execute_process(COMMAND "/home/loi/Vehicle_Motion_Playground/03_VMEnv/02_ros-bridge/build/ros-bridge/carla_waypoint_publisher/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/loi/Vehicle_Motion_Playground/03_VMEnv/02_ros-bridge/build/ros-bridge/carla_waypoint_publisher/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
