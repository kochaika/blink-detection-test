import Jetson.GPIO as GPIO
import time

# Pin Definitions
output_pin = 18  # BCM pin 18, BOARD pin 12
pins = [17,18,27,23]

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    for i in pins:
        GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)


    #self test

    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            for i in pins:
                GPIO.output(i, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(i, GPIO.LOW)
                time.sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
