#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64,Float32
import time

pub = None
def callback(msg):
    m = Float64()
    m.data = msg.data
    pub.publish(m)

if __name__ == '__main__':
    global pub
    rospy.init_node('float_converter')
    pub = rospy.Publisher('feedback_val2', Float64, queue_size=10)
    rospy.Subscriber('feedback_val', Float32,callback)
    rate = rospy.Rate(60) #60 Hz

    while not rospy.is_shutdown():
        rospy.spin()
