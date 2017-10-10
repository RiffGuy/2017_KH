import RPi.GPIO as GPIO
import time
import threading

class suvomoter():
    def open(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        self.p = GPIO.PWM(26, 50)
        self.p.start(8)
        self.p.ChangeDutyCycle(8)
        self.p.ChangeDutyCycle(2.7) # up
        time.sleep(5)
        self.p.ChangeDutyCycle(8) # down
        time.sleep(1)
        GPIO.setup(26, GPIO.IN)
        #time.sleep(2)
        #p.ChangeDutyCycle(2.7)
        #time.sleep(2)