import RPi.GPIO as GPIO
import time
import threading
import cnn
import suvomoter
from PyQt5 import QtGui

class pir(threading.Thread):
    def run(self):
        GPIO.setmode(GPIO.BCM)
        sv = suvomoter.suvomoter()
        sensor = 4
        
        window = QtGui.QWindow()
        window.setGeometry(0,0,100,100)

        GPIO.setup(sensor, GPIO.IN)
        GPIO.setup(12, GPIO.OUT)
        np = cnn.CNN()
        accounts = np.nb_classes
        time.sleep(2)
		
        while True:
            #if accounts != record.VOICE_RECORD().account_number:
            #    np.build()
            if GPIO.input(sensor) :
                #print GPIO.input(sensor)
                print ("no detected")
                #time.sleep(1)
            else : 
                print ("detected")
                GPIO.output(12, True)
                rst = np.predict()
                GPIO.output(12, False)
                if rst!=-1:
                    sv.open()
                #time.sleep(1)
            time.sleep(0.2)

