#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('sender_speed')
pub = rospy.Publisher('speed_topic', String)
pub = rospy.Publisher('speed_topic', String)

rate = rospy.Rate(1)

idx = 0
pub_size = [1000000] # 1M = 1000000byte
pub_size += [5000000] # 5M
pub_size += [10000000] # 10M
pub_size += [20000000] # 20M
pub_size += [50000000] # 50M


# data = "#" * pub_size
while (pub.get_num_connections() == 0):
    pass

while not rospy.is_shutdown():
    try:
        data = "#" * pub_size[idx]; 
    except IndexError:
        idx = 0
        data = "#" * pub_size[idx]; 
    idx += 1

    # print(len(data), data/1000000+"M")

    pub.publish(data + ":" + str(rospy.get_time()))
    rate.sleep()
