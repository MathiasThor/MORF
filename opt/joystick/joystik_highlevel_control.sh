#!/bin/bash

source /opt/ros/melodic/setup.bash 
source /home/morf-one/catkin_ws/devel/setup.bash

exec roslaunch joy_demostarter joy_demostarter.launch

sleep 5

