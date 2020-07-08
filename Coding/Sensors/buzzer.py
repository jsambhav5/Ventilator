#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 7 as output
buzzer=4
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
while True:
    try:
        GPIO.output(buzzer,GPIO.HIGH)
        print ("Beep")
        sleep(0.8) # Delay in seconds
        GPIO.output(buzzer,GPIO.LOW)
        print ("No Beep")
        sleep(0.2)
    except KeyboardInterrupt:
        GPIO.output(buzzer, GPIO.Low)
        GPIO.cleanup()