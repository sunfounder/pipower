#!/usr/bin/env python3
# Safe shutdown example
# Change the pin numbers to match your setup

import RPi.GPIO as GPIO
import time
import os

VUSB_PIN = 17
CHG_PIN = 18
LO_DT_PIN = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(VUSB_PIN, GPIO.IN)
    GPIO.setup(CHG_PIN, GPIO.IN)
    GPIO.setup(LO_DT_PIN, GPIO.IN)

if __name__ == '__main__':
    setup()

    while True:
        charging = GPIO.input(CHG_PIN)
        low_battery = GPIO.input(LO_DT_PIN)
        external_power = GPIO.input(VUSB_PIN)
        # If it's not charging and the battery is low, shut down the pi
        # Even if the external power is connected, no charging means the power supply is not strong enough
        if not charging and low_battery:
            # Do some stuff before shutting down

            # Shutdown
            print("Shutting down...")
            time.sleep(1)
            os.system("sudo shutdown -h now")
            break
        
        # You don't need that fast to check the states
        time.sleep(2)
