#!/usr/bin/env python3
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

"""
Button Driver

License:
Copyright 2021-2025 - Arjun Kannan
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
...
"""

import time
import Adafruit_BBIO.GPIO as GPIO

HIGH = GPIO.HIGH
LOW = GPIO.LOW

class Button():
    """ Button Class """
    def __init__(self, pin=None, press_low=True, sleep_time=0.1):
        if pin is None:
            raise ValueError("Pin not provided for Button()")
        self.pin = pin
        self.unpressed_value = HIGH if press_low else LOW
        self.pressed_value = LOW if press_low else HIGH
        self.sleep_time = sleep_time
        self.press_duration = 0.0
        self._setup()

    def _setup(self):
        """ Setup the hardware components. """
        GPIO.setup(self.pin, GPIO.IN)

    def is_pressed(self):
        """ Check if the button is pressed. """
        return GPIO.input(self.pin) == self.pressed_value

    def wait_for_press(self):
        """ Wait for the button to be pressed. """
        button_press_time = None
        while GPIO.input(self.pin) == self.unpressed_value:
            time.sleep(self.sleep_time)
        button_press_time = time.time()
        while GPIO.input(self.pin) == self.pressed_value:
            time.sleep(self.sleep_time)
        self.press_duration = time.time() - button_press_time

    def get_last_press_duration(self):
        return self.press_duration

    def cleanup(self):
        GPIO.cleanup()

if __name__ == '__main__':
    print("Button Test")
    button = Button("P2_2")
    try:
        print("Is the button pressed?")
        print(" {0}".format(button.is_pressed()))
        print("Press and hold the button.")
        time.sleep(4)
        print("Is the button pressed?")
        print(" {0}".format(button.is_pressed()))
        print("Release the button.")
        time.sleep(4)
        print("Waiting for button press ...")
        button.wait_for_press()
        print(" Button pressed for {0} seconds.".format(button.get_last_press_duration()))
    except KeyboardInterrupt:
        pass
    print("Test Complete")
