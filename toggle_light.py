import RPi.GPIO as GPIO
import time


def toggle(pin=17):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(pin, GPIO.LOW)


if __name__ == "__main__":
    toggle()
