#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('sender_serial')
pub = rospy.Publisher('serial_topic', Int32)

rate = rospy.Rate(2)
count = 1

while (pub.get_num_connections() == 0):
    pass

while not rospy.is_shutdown():
    pub.publish(count)
    count+=1
    rate.sleep()