#!/usr/bin/env python

RPI = False

import rospy
from std_msgs.msg import Int64
from time import sleep

if RPI:
    from RPi import GPIO

clk = 11
dt = 12

if RPI:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

def encoder_data():
    global counter, clkState, clkLastState, dtState, clk, dt
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != clkLastState:
        if dtState != clkState:
                counter += 1
        else:
                counter -= 1
        pub.publish(counter)
    clkLastState = clkState

if __name__ == '__main__':
  global rpm
  rospy.init_node('feedback_val')
  last_time = rospy.Time.now()
  pub = rospy.Publisher('encoder_val', Int64, queue_size=10)

  while not rospy.is_shutdown():
    encoder_data()

  GPIO.cleanup()
