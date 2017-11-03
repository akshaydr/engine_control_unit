#!/usr/bin/env python

RPI = False

import rospy
from std_msgs.msg import Float32
import time

if RPI:
  import RPi.GPIO as GPIO
  GPIO.setmode(GP, IO.BOARD)
  GPIO.setup(sensor, GPIO.IN)

current_time = rospy.Time()
last_time = rospy.Time
state = 0
prevState = 0
counter = 0.0

sensor = 4


def get_rpm():
  if RPI:
    sensor_val = GPIO.input(sensor)

  if (sensor_val > 650):
    state = 1
  else:
    state = 0
  if (state != prevState):
    if(state == 1):
      counter += 1
    prevState = state

  while (last_time - startTime) > 0.1:
    print counter / 6
    counter = 0
    startTime = last_time


if __name__ == '__main__':
  global counter
  rospy.init_node('feedback_val')
  pub = rospy.Publisher('feedback_val', Float32, queue_size=10)

  while not rospy.is_shutdown():
    get_rpm()
    pub.publish(counter)
    rospy.spin()
