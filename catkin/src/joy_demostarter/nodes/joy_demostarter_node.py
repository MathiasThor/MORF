#!/usr/bin/env python
from __future__ import print_function, division

import os
import rospy
from sensor_msgs.msg import Joy


class JoyDemoStarter(object):

    def __init__(self):
        print ("node started")
        rospy.Subscriber("joy", Joy, self.joyCallback)
        self.driver_running = False

    def joyCallback(self, data):
        if data.axes[7] == -1 and data.buttons[0] == 1:
            if self.driver_running:
            	os.system("sudo systemctl start morf-controller.service")
	    	os.system("blinkstick --set-color red --brightness 10") 
            	print ("Starting Controller")
	    else:
	 	os.system("blinkstick orange --pulse --duration 250 --repeats 2 --brightness 50")
                os.system("blinkstick orange --brightness 10")
        elif data.axes[7] == -1 and data.buttons[1] == 1:
	    if self.driver_running: 	
		os.system("sudo systemctl stop morf-controller.service") 
            	os.system("blinkstick green --brightness 10") 
            	print ("Terminating Controller")
            else:
                os.system("blinkstick orange --pulse --duration 250 --repeats 2 --brightness 50")
                os.system("blinkstick orange --brightness 10")
        elif data.axes[7] == -1 and data.buttons[3] == 1:
            os.system("sudo systemctl start dynamixel_driver.service")
            os.system("blinkstick green --brightness 10")
	    self.driver_running = True  
            print ("Starting Driver")
        elif data.axes[7] == -1 and data.buttons[4] == 1:
            os.system("sudo systemctl stop dynamixel_driver.service") 
            os.system("sudo systemctl stop morf-controller.service") 
            os.system("blinkstick orange --brightness 10") 
	    print ("Terminating Driver")
	    self.driver_running = False

def main():
    rospy.init_node('joy_demostarter')
    node = JoyDemoStarter()
    rospy.spin()


if __name__ == '__main__':
    main()
