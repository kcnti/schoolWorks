import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
channel_input = []
channel_output = []

for x in channel_input:
    GPIO.setup(channel_input,GPIO.IN)
for y in channel_output:
    GPIO.setup(channel_output,GPIO.OUT)

while(True):
    button1 = GPIO.input(5)
    if button1 == False:
        GPIO.output(5,1)    #light on
        time.sleep(0.2)
    else:
        GPIO.output(5,0)    #light off
        time.sleep(0.2)
    button2 = GPIO.input(3)
    if button2 == False:
        GPIO.output(3,1)
        time.sleep(0.2)
    else:
        GPIO.output(3,0)
        time.sleep(0.2)
    button3 = GPIO.input(11)
    if button3 = False:
        GPIO.output(11,1)
        time.sleep(0.2)
    else:
        GPIO.output(11,0)
        time.sleep(0.2)