# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time
import subprocess

#from board import SCL, SDA
#import busio
from PIL import Image, ImageDraw, ImageFont
#import adafruit_ssd1306
import Adafruit_SSD1306
import Jetson.GPIO as GPIO


# Create the I2C interface.
#i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
#disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_bus=1, gpio=1)

# Clear display.
disp.begin()
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)
actions = {'red':27, 'yellow':18, 'green':17, 'beep':23}
for i in actions:
    GPIO.setup(actions[i], GPIO.OUT, initial=GPIO.LOW)

#val = GPIO.LOW
try:
    while True:
        for i in actions:
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((x, top + 0), i, font=font1, fill=255)
            #draw.text((x, top + 16), ">.<", font=font1, fill=255)
        # Display image.
            disp.image(image)
            disp.display()
            GPIO.output(actions[i], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(actions[i], GPIO.LOW)
            time.sleep(0.5)

finally:
    GPIO.cleanup()
