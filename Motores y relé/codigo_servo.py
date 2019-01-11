import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(25,GPIO.OUT) # Pin 25 como salida
p = GPIO.PWM(25,50)
p.start(7.5)
time.sleep(2)

try:
    while True:
        p.ChangeDutyCycle(4.5)
        time.sleep(2)

        p.ChangeDutyCycle(10.5)
        time.sleep(2)

        p.ChangeDutyCycle(7.5)
        time.sleep(2)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    
