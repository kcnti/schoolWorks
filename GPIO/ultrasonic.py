import RPi.GPIO as GPIO
import time

TRIG = #ส่งคลื่นเสียง
ECHO = #รับคลื่นเสียง
portLED = []

GPIO.setmode(GPIO.BOARD)
for x in portLED:
    GPIO.setup(x,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.OUT)

while(True):
    GPIO.output(TRIG,False) #Still Close
    time.sleep(1)
    GPIO.output(TRIG,True) #Sending sounds Frequen
    time.sleep(0.00001)
    GPIO.output(TRIG,False) #Close

    while(GPIO.input(ECHO) == 0):
        stpulse = time.time() #Save time when sound frequen start
    while(GPIO.input(ECHO) == 1):
        endpulse = time.time() #Save time when sound frequen end
    
    duration = endpulse - stpulse #like delta T
    distance = duration * 17150
    distance = round(distance,2) #ปัดเศษทศนิยม 2 จุด

    print("Distance:",distance,"cm")

    if distance >= 5 and distance <= 20:
        for x in range(5):    
            GPIO.output(portLED,1)
            time.sleep(0.2)
            GPIO.output(portLED,0)
            time.sleep(0.2)
    if distance > 20 and distance <= 50:
        for i range(4):
            GPIO.output(portLED[i],portLED[7-i],1)
            time.sleep(0.2)
            GPIO.output(portLED[i],portLED[7-i],0)
            time.sleep(0.2)
    if distance > 50 and distance <= 100:
        for x in portLED:
            if x % 2 == 0:
                GPIO.output(x,1)
                time.sleep(0.2)
                GPIO.output(x,0)
                time.sleep(0.2)
            elif x % 2 == 1:
                GPIO.output(x,1)
                time.sleep(0.2)
                GPIO.output(x,0)
                time.sleep(0.2)
    if distance > 100 and distance <= 150:
        GPIO.output(portLED,1)
        for x in portLED:
            GPIO.output(portLED,0)
            time.sleep(0.2)
    elif distance > 150:
        GPIO.output(portLED,0)