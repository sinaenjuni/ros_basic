#!/usr/bin/env python

import rospy
import time
from my_msg.msg import motor
from std_msgs.msg import Header

motor_control = motor()
header = Header()


rospy.init_node('auto_dvicer')
pub = rospy.Publisher('motor', motor, queue_size=1)

def motor_pub(angle, speed):
    motor_control.angle = angle
    motor_control.speed = speed

    header.stamp = rospy.Time.now()
    motor_control.header = header
    pub.publish(motor_control)

speed = 3
while not rospy.is_shutdown():
    angle = -50
    for i in range(60):
        motor_pub(angle, speed)
        time.sleep(0.1)

    angle = 0
    for i in range(30):
        motor_pub(angle, speed)
        time.sleep(0.1)

    angle = 50
    for i in range(60):
        motor_pub(angle, speed)
        time.sleep(0.1) 

    angle = 0
    for i in range(30):
        motor_pub(angle, speed)
        time.sleep(0.1)
    