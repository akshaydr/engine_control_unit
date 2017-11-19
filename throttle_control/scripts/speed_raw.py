#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

vehicle_speed = 250

if __name__ == '__main__':
    rospy.init_node('speed')
    pub = rospy.Publisher('speed_raw', Int32, queue_size=10)
    rate = rospy.Rate(10)
    # vehicle_speed = input("Enter speed of the vehicle:")


    while not rospy.is_shutdown():
        rate.sleep()
        pub.publish(vehicle_speed)
