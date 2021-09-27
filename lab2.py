import RPi.GPIO as GPIO
from time import sleep
p1=4
p2=17
p3=2
in1,in2=23,24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 
GPIO.setup(in1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.output(p3, 1)
try:
  def myCallback(pin):  
    if pin==in1:
      pwm = GPIO.PWM(p1, 100)
      pwm.start(0)
      while 1:
        for dc in range(101):
          pwm.ChangeDutyCycle(dc)
          sleep(0.01)
    if pin==in2:
      pwm = GPIO.PWM(p2, 100)
      pwm.start(0)
      while 1:
        for dc in range(101):
          pwm.ChangeDutyCycle(dc)
          sleep(0.01)
  GPIO.add_event_detect(in1,GPIO.RISING,callback=myCallback,bouncetime=100)
  GPIO.add_event_detect(in2,GPIO.RISING,callback=myCallback,bouncetime=100)
except KeyboardInterrupt:
  print('\nExiting')
GPIO.cleanup()