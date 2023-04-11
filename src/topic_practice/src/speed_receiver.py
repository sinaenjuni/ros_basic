#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    # print(msg.data)
    curren_time = str(rospy.get_time())
    data, arrival_time = str(msg.data).split(':')

    time_diff = float(curren_time) - float(arrival_time)
    string_size = len(data)
    rospy.loginfo(str(string_size) + " byte: " + str(time_diff) + " second")
    try:
        rospy.loginfo("speed: " + str(float(string_size)/time_diff) + "byte/s")
    except ZeroDivisionError:
        rospy.loginfo("speed: " + str(float(string_size)/time_diff) + "byte/s")
rospy.init_node('receiver_speed')
rospy.loginfo("init")
sub = rospy.Subscriber('speed_topic', String, callback)

rospy.spin()