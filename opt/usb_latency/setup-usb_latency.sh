#!/bin/bash
echo "Setting up usb_latency ..."

sudo usermod -aG dialout $USER
echo 1 | sudo tee /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
echo 1 | sudo tee /sys/bus/usb-serial/devices/ttyUSB1/latency_timer
