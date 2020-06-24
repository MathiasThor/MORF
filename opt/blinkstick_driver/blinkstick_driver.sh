#!/bin/bash

source /opt/ros/melodic/setup.bash 
source /home/morf-one/catkin_ws/devel/setup.bash

exec roslaunch ros_blinkstick_square_driver ros_blinkstick_square_driver.launch
#exec roslaunch ros_imu_driver ros_imu_driver.launch
#exec roslaunch my_dynamixel_workbench_tutorial dynamixel_driver.launch
sleep 5
