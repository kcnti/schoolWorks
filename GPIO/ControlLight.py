import RPi.GPIO as GPIO
import time

channel =
outs =
GPIO.setmode(GPIO.BOARD)
for x in channel:
    GPIO.setup(channel,GPIO.IN)
for y in outs:
    GPIO.setup(outs,GPIO.OUT)

while(True):
    button1 = GPIO.input()
    if button1 == False:
        GPIO.output(channel,1)
        time.sleep(0.2)
    else:
        GPIO.output(channel,0)
        time.sleep(0.2)