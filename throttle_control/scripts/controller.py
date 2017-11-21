#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from std_msgs.msg import String
import tf
import time

set_speed = 0
feedback_speed = 0.0
direction = -0.135
current_time = rospy.Time()
# e_speed_sum = 0.0
# e_speed_pre = 0.0
# kp =
# ki =
# kd =

def speed_cb(msg):
    global set_speed
    set_speed = msg.data
    # rospy.loginfo(set_speed)

def feedback_cb(msg):
    global feedback_speed
    feedback_speed = msg.data
    # print("controlle_val=",feedback_speed)

def pid_control():
  global set_speed, feedback_speed, direction, e_speed, e_speed_sum, e_speed_pre, kp, ki, kd
  current_time = rospy.Time.now()
  odom_broadcaster = tf.TransformBroadcaster()
  e_speed = set_speed - feedback_speed

  # PID code. need to be modified based on the required application.
  # e_speed = set_speed - feedback_speed;
  # pwm_pulse = e_speed*kp + e_speed_sum*ki + (e_speed - e_speed_pre)*kd;
  # e_speed_pre = e_speed;  //save last (previous) error
  # e_speed_sum += e_speed; //sum of error
  # if (e_speed_sum >4000) e_speed_sum = 4000;
  # if (e_speed_sum <-4000) e_speed_sum = -4000;

  # rospy.loginfo(e_speed)
  if (e_speed > 50):
    pub.publish("cw")
    # rospy.loginfo("Move cw")
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )
    direction += 0.00012

  elif (e_speed < -50):
    pub.publish("ccw")
    # rospy.loginfo("Move ccw")
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )
    direction -= 0.00012

  elif (e_speed > -50 and e_speed < 50):
    pub.publish("stop")
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    odom_broadcaster.sendTransform(
        (direction,0.02,-0.016),
        odom_quat,
        current_time,
        "base_link",
        "nut_assem"
    )

if __name__ == '__main__':
  rospy.init_node('controller')
  pub = rospy.Publisher('dirver_val', String, queue_size=10)
  rospy.Subscriber('speed_raw', Int32, speed_cb)
  rospy.Subscriber('feedback_val', Float32, feedback_cb)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    pid_control()
    rate.sleep()
