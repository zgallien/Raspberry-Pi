"""
This is a simple implementation of Python's RPi.GPIO module

Depending on argument [1], the script will either:
- turn on red, green, and then blue LEDs in succession in an endless loop
- turn on red LEDs
- turn on green LEDs
- turn on blue LEDs
- turn off LED Strip
"""

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class RGBStrip(object):
    """
    An instance of RGBStrip will have three GPIO pins configured for
    red, green, and blue LEDs. Class methods allow User to set LED
    strip to a specific color, off, or cycle through RGB.
    """
    def __init__(self, red_pin, green_pin, blue_pin):

        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.setup_pins()

    def setup_pins(self):
        """
        Tell rPi what pin is used as GPIO output for each LED color
        """
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

    def rgb_cycle(self):
        """
        Cycle through each RGB color
        """
        while True:

            self.red_on()
            time.sleep(5)
            self.strip_off()

            self.green_on()
            time.sleep(5)
            self.strip_off()

            self.blue_on()
            time.sleep(5)
            self.strip_off()

    def red_on(self):
        """
        Turn on red LED
        """
        GPIO.output(self.red_pin, 50)

    def green_on(self):
        """
        Turn on green LED
        """
        GPIO.output(self.green_pin, 50)

    def blue_on(self):
        """
        Turn on blue LED
        """
        GPIO.output(self.blue_pin, 50)

    def strip_off(self):
        """
        Turn all LEDs off
        """
        GPIO.output(self.red_pin, 0)
        GPIO.output(self.green_pin, 0)
        GPIO.output(self.blue_pin, 0)


if __name__ == '__main__':

    rgb = RGBStrip(27, 17, 22)

    try:

        if sys.argv[1].lower() == 'red':

            rgb.red_on()

        elif sys.argv[1].lower() == 'green':

            rgb.green_on()

        elif sys.argv[1].lower() == 'blue':

            rgb.blue_on()

        elif sys.argv[1].lower() == 'cycle':

            rgb.rgb_cycle()


        elif sys.argv[1].lower() not in ['red', 'green', 'blue', 'cycle']:

            print 'Did not recognize {} argument. Please use on of the following:' \
                  '\nred' \
                  '\ngreen' \
                  '\nblue' \
                  '\ncycle'.format(
                            sys.argv[1]
                            )

    except IndexError as e:

        print '{}' \
              '\nPlease run again and use one of the following as an argument:' \
              '\nred' \
              '\ngreen' \
              '\nblue' \
              '\ncycle'.format(e)
