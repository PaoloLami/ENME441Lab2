import RPi.GPIO as GPIO
from time import sleep
p1=4
p2=17
p3=27
in1,in2=23,24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 
GPIO.setup(in1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.output(p1, 1)
sleep(10)
