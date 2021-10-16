#เปิดแล้วปิดไฟ

import RPi.GPIO as GPIO
import time

channel = 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.OUT)

while(True):
    for x in channel:
        GPIO.output(x,1)
        time.sleep(0.2)
        GPIO.output(x,0)
        time.sleep(0.2)