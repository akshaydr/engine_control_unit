#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32

positon = 0.0

def distance_calc(speed):
    position = speed # Equation to calculate vehicle speed
    print('Distance =', position)
    pub.publish(position)

def callback(msg):
    vehicle_speed = msg.data
    distance_calc(vehicle_speed)

if __name__ == '__main__':
    rospy.init_node('speed_preprocessor')
    rospy.Subscriber('speed_raw', Int32, callback)
    pub = rospy.Publisher('position', Float32, queue_size=10)

    while not rospy.is_shutdown():
        rospy.spin()
