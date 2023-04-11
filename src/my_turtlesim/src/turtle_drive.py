#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_turtlesim_node', anonymous=True) # make node
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # make publisher

msg = Twist()
msg.linear.x = 2.0
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 1.8

rate = rospy.Rate(1)  
# number of message per 1 second

while not rospy.is_shutdown():  
    # message publish
    pub.publish(msg)
    rate.sleep()