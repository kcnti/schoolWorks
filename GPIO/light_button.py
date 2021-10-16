import RPi.GPIO as GPIO
import time

channel = 
channel_out = 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel_out,GPIO.OUT)

while(True):
    state = GPIO.input(channel)
    if state == False: #ยังไม่กดปุ่มจะเปิดไฟ
        GPIO.output(channel_out,GPIO.HIGH)
        time.sleep(0.2)
    else:
        GPIO.output(channel_out,GPIO.LOW)
        time.sleep(0.2)