#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node("change_fid")
pub = rospy.Publisher("/scan_fid", LaserScan)
def callback(msg):
    msg.header.frame_id = "base_link"
    pub.publish(msg)
    print(msg)
rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()