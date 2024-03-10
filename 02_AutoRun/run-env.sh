# cd /opt/carla-simulator/&&
# ./CarlaUE4.sh -quality=High -frame=60&&

# cd /home/loi/01_CarAutoParking/02_Controller/02_ros-bridge/&&
# source devel/setup.bash&&
# roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch&&

# cd /home/loi/01_CarAutoParking/02_Controller/01_carla-parking-master;
# source devel/setup.bash;
# cd src/carla_park/src/;
# python3 main.py;

# cd /home/loi/01_CarAutoParking/01_UI/rasp_ver/src;
# python3 GUI_QML_main.py

# chmod +x low-carla.sh
# /home/letruyen/VehicleMotionPlayground/02_AutoRun/low-carla.sh
gnome-terminal -x ./low-carla.sh
echo "wait for 10 seconds"
sleep 10s
gnome-terminal --tab --title="roscore" --command="roscore"
sleep 2s
gnome-terminal --tab --title="bridge" --command="python3 ../01_VMEnv/01_RosBridge/src/ros-bridge/carla_ros_bridge/src/carla_ros_bridge/bridge.py"
sleep 3s
gnome-terminal --tab --title="application" --command="python3 ../01_VMEnv/02_ClientSide/main.py"
# gnome-terminal -x /home/loi/02_RunDemo/auto-parking.sh
# gnome-terminal -x /home/loi/02_RunDemo/door-open-warning.sh
# gnome-terminal -x /home/loi/02_RunDemo/sleep-detector-carla.sh