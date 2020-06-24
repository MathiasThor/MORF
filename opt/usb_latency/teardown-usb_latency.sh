#!/bin/bash
echo "Tearing down usb_latency ..."
if [ -f /tmp/usb_latency-activated ]; then
    rm /tmp/usb_latency-activated
else
    echo "Doesnt seem to be up: Skipping ..."
fi
