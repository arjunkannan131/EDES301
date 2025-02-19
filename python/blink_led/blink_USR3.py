""#!/usr/bin/env python3
"""
blink_USR3.py

This script blinks the USR3 LED on the BeagleBone board at a frequency of 5 Hz (5 full on/off cycles per second) 
using the Adafruit_BBIO library.

Author: Arjun Kannan
Course: EDES301
License: MIT
"""

import Adafruit_BBIO.GPIO as GPIO
import time

# Define the LED pin
USR3 = "USR3"

# Set up the LED pin as an output
GPIO.setup(USR3, GPIO.OUT)

# Blink frequency and delay calculation
frequency = 5  # Hz
period = 1.0 / frequency  # Total time for one cycle
half_period = period / 2  # Time for LED to stay on/off

try:
    while True:
        GPIO.output(USR3, GPIO.HIGH)  # Turn LED on
        time.sleep(half_period)
        GPIO.output(USR3, GPIO.LOW)   # Turn LED off
        time.sleep(half_period)
except KeyboardInterrupt:
    print("\nExiting gracefully...")
    GPIO.cleanup()  # Cleanup GPIO settings on exit

