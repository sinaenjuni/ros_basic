#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print(msg.data)

rospy.init_node('receiver_serial')
sub = rospy.Subscriber('serial_topic', Int32, callback)

rospy.spin()