import RPi.GPIO as gpio
from time import sleep
p1=4
p2=17
p3=27
in1,in2=23,24
gpio.setmode(gpio.BCM)
gpio.setup(p1, GPIO.OUT) 
gpio.setup(p2, GPIO.OUT) 
gpio.setup(p3, GPIO.OUT) 
gpio.setup(in1,gpio.IN,pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2,gpio.IN,pull_up_down=gpio.PUD_DOWN)
try:
  while True:
    GPIO.output(p3, 0)
    sleep(0.5)
    GPIO.output(p3, 1)
    sleep(0.5)
  def myCallback(pin):  
    if pin == in1:
      pwm = GPIO.PWM(p1, 100)
      try:
        pwm.start(0)
        while 1:
          for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            sleep(0.01)
      except KeyboardInterrupt:
        print('\nExiting')
    if pin == in2:
      pwm = GPIO.PWM(p2, 100)
      try:
        pwm.start(0)
        while 1:
          for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            sleep(0.01)
      except KeyboardInterrupt:
        print('\nExiting')
  gpio.add_event_detect(in1,gpio.RISING,callback=myCallback,bouncetime=100)
  gpio.add_event_detect(in2,gpio.RISING,callback=myCallback,bouncetime=100
except KeyboardInterrupt:
  print('\nExiting')
gpio.cleanup()