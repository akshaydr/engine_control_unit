#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

vehicle_speed = 0

if __name__ == '__main__':
    rospy.init_node('speed')
    pub = rospy.Publisher('speed_raw', Int32, queue_size=10)

    vehicle_speed = input("Enter speed of the vehicle:")
    pub.publish(vehicle_speed)

    while not rospy.is_shutdown():
        rospy.spin()
