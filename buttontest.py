import RPi.GPIO as GPIO
import time
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
def myCallback(pin):
  if pin==in1:
    GPIO.output(p1,1)
    time.sleep(2)
    GPIO.output(p1,0)
  if pin==in2:
    GPIO.output(p2,1)
    time.sleep(2)
    GPIO.output(p2,0)   
GPIO.add_event_detect(in1,GPIO.RISING,callback=myCallback,bouncetime=500)
GPIO.add_event_detect(in2,GPIO.RISING,callback=myCallback,bouncetime=500)
while True:
  print('.', end='')
  time.sleep(0.1)
GPIO.cleanup()