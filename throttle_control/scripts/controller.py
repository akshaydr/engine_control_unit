#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from std_msgs.msg import String
import time

set_speed = 0
feedback_speed = 0.0


def speed_cb(msg):
  set_speed = msg.data


def feedback_cb(msg):
  feedback_speed = msg.data


def pid_control():
  global set_speed, feedback_speed
  diff = set_speed - feedback_speed

#   PID code. need to be modified based on the required application.
   # e_speed = set_speed - pv_speed;
   # pwm_pulse = e_speed*kp + e_speed_sum*ki + (e_speed - e_speed_pre)*kd;
   # e_speed_pre = e_speed;  //save last (previous) error
   # e_speed_sum += e_speed; //sum of error
   # if (e_speed_sum >4000) e_speed_sum = 4000;
   # if (e_speed_sum <-4000) e_speed_sum = -4000;

  if (diff > 0):
    pub.publish("cw")
  else:
    pub.publish("ccw")


if __name__ == '__main__':
  rospy.init_node('controller')
  pub = rospy.Publisher('dirver_val', String, queue_size=10)
  rospy.Subscriber('speed_raw', Int32, speed_cb)
  rospy.Subscriber('feedback_val', Float32, feedback_cb)

  while not rospy.is_shutdown():
    pid_control()
    rospy.spin()
