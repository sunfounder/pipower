# Read all states of PiPower
# Change the pin numbers to match your setup

import RPi.GPIO as GPIO
import time

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
        # Check if external power is connected
        if GPIO.input(VUSB_PIN):
            print("External power connected")
        else:
            print("External power disconnected")

        # Check if battery is charging
        if GPIO.input(CHG_PIN):
            print("Charging")
        else:
            print("Not charging")

        # Check if battery is low
        if GPIO.input(LO_DT_PIN):
            print("Low battery")
        else:
            print("Battery OK")

        time.sleep(2)
