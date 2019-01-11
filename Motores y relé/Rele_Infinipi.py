import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

while True:
    command = raw_input("1 para encender el relè, 0 para apagarlo: ")

    if command == "1":
        GPIO.output(22, True)
    elif command == "0":
        GPIO.output(22, False)
