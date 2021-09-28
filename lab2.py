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
try:
  def myCallback(pin):
    if pin==in1:
      pwn1=GPIO.PWM(p1,100)
      pwn1.start(0)
      for dc in range(101):
        pwm1.ChangeDutyCycle(dc)
        sleep(0.1)
    if pin==in2:
      pwn2=GPIO.PWM(p1,100)
      pwn2.start(0)
      for dc in range(101):
        pwm2.ChangeDutyCycle(dc)
        sleep(0.1)
  GPIO.add_event_detect(in1,GPIO.FALLING,callback=myCallback,bouncetime=500)
  GPIO.add_event_detect(in2,GPIO.FALLING,callback=myCallback,bouncetime=500)
  while True:
    GPIO.output(p3, 0)
    sleep(0.5)
    GPIO.output(p3, 1)
    sleep(0.5)
except KeyboardInterrupt:
  print('\nExiting')
GPIO.cleanup()