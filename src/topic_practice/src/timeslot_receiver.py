#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


rospy.init_node("timeslot_receiver_node", anonymous=True)

def callback(msg):
    print(msg.damsg.datata)
sub = rospy.Subscriber('timeslot_topic', Int32, callback, queue_size=10)


rospy.spin()
