#!/usr/bin/python

import time
import pigpio

pi = pigpio.pi()

pi.set_mode(25, pigpio.OUTPUT)

pi.set_sevo_pulsewidth(25,1500)
time.sleep(1)

for i in range(5):
    pi.set_sevo_pulsewidth(25,2500)
    time.sleep(1)
    pi.set_sevo_pulsewidth(25,600)
    time.sleep(1)
    pi.set_sevo_pulsewidth(25,1500)
    time.sleep(1)

pi.set_sevo_pulsewidth(25,0)

pi.stop()
