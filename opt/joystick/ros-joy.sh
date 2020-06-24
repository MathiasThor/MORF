#!/bin/bash

source /opt/ros/melodic/setup.bash 
source /home/morf-one/catkin_ws/devel/setup.bash

sleep 10
exec rosrun joy joy_node
#exec roslaunch ros_imu_driver ros_imu_driver.launch
#exec roslaunch my_dynamixel_workbench_tutorial dynamixel_driver.launch
sleep 5

