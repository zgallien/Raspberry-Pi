import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class RGBStrip(object):

    def __init__(self, red_pin, green_pin, blue_pin):

        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.setup_pins()

    def rgb_on(self):

        # r_intensity = 0
        # g_intensity = 0
        # b_intensity = 0

        print 'TEST 1: Red only'

        GPIO.output(self.red_pin, 50)
        GPIO.output(self.green_pin, 0)
        GPIO.output(self.blue_pin, 0)

        print 'TEST 2: Add Green'

        GPIO.output(self.red_pin, 50)
        GPIO.output(self.green_pin, 50)
        GPIO.output(self.blue_pin, 0)


        print 'TEST 3: Add Blue'

        GPIO.output(self.red_pin, 50)
        GPIO.output(self.green_pin, 50)
        GPIO.output(self.blue_pin, 50)

        print 'TEST 4: Red going up'

        red_intensity = 0

        while red_intensity < 255:

            GPIO.output(self.red_pin, red_intensity)

            red_intensity += 1
            time.sleep(.25)

            print 'red_intensity: {}'.format(red_intensity)



        # while True:
        #
        #     GPIO.output(self.red_pin, r_intensity)
        #     GPIO.output(green_pin, g_intensity)
        #     GPIO.output(blue_pin, b_intensity)
        #
        #     r_intensity += 1
        #     g_intensity += 1
        #     b_intensity += 1
        #
        #     if r_intensity == 255:
        #         r_intensity = 0
        #     elif g_intensity == 255:
        #         g_intensity = 0
        #     elif b_intensity == 255:
        #         b_intensity = 0

        self.rgb_off()



    def rgb_off(self):

        GPIO.output(self.red_pin, 0)
        GPIO.output(self.green_pin, 0)
        GPIO.output(self.blue_pin, 0)

        time.sleep(3)


    def setup_pins(self):

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

if __name__ == '__main__':

    rgb = RGBStrip(27, 17, 22)

    # rgb.rgb_on()

    rgb.rgb_off()
