#!/usr/bin/env python

RPI = True

import rospy
from std_msgs.msg import Float32
import time

sensor = 3

if RPI:
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(sensor, GPIO.IN)

last_time = rospy.Time()
state = 0
prevState = 0
counter = 0.0
sensor_val = 0
val = 0

def get_rpm():
  global current_time, last_time, state, prevState, counter, sensor, sensor_val

  current_time = rospy.Time.now()

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
  
  val = (current_time - last_time).to_sec()
  print (val)
#  if (val > 0.1):
#    print counter / 6
#    counter = 0
#    last_time = current_time


if __name__ == '__main__':
  global counter
  rospy.init_node('feedback_val')
  last_time = rospy.Time.now()
  pub = rospy.Publisher('feedback_val', Float32, queue_size=10)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
    get_rpm()
    pub.publish(counter)
    rate.sleep()
