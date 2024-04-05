import RPi.GPIO as GPIO
import time

pins = [17,27,22,26]

def setupPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)
    
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    
def progressBar(pin):
    for p in range(0,pin):
        GPIO.output(pins[p],GPIO.HIGH)
       
def blink(n):
    for i in range(0,n+1):
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(0.5)
    
setupPins()
for p in range(0,5):
    progressBar(p)
    time.sleep(2)
blink(3)


#turn = int(input ("enter distance to turn"))
'''if turn < 10:
    progressBar(4)
elif turn>10 and turn<20:
    progressBar(3)
elif turn>20 and turn<40:
    progressBar(2)
elif turn>40 and turn<100:
    progressBar(1)'''