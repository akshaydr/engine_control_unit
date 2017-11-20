#!/usr/bin/env python

RPI = True

import rospy
from std_msgs.msg import String
import time

if RPI:
  import RPi.GPIO as GPIO

if RPI:
  GPIO.setmode(GPIO.BOARD)

  M1pwm = 12
  M1dir = 5  # Motor 1

  GPIO.setup(M1pwm, GPIO.OUT)
  GPIO.setup(M1dir, GPIO.OUT)

  GPIO.output(M1pwm, GPIO.LOW)
  GPIO.output(M1dir, GPIO.LOW)

  pwm1 = GPIO.PWM(M1pwm, 1)
else:
  print("Simulated setup done!")


def callback(msg):
  rospy.loginfo(msg.data)
  if RPI:
    if (msg.data == "cw"):
      pwm1.start(50)
      GPIO.output(M1dir, GPIO.HIGH)

    elif (msg.data == "ccw"):
      pwm1.start(50)
      GPIO.output(M1dir, GPIO.LOW)

    else:
      pwm.stop()


if __name__ == '__main__':
  rospy.init_node('driver')
  rospy.Subscriber('dirver_val', String, callback)

  while not rospy.is_shutdown():
    rospy.spin()
if RPI:
  GPIO.cleanup()
