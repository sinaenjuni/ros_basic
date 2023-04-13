#! /usr/bin/env python

import rospy
from my_msg.msg import motor
from sensor_msgs.msg import JointState

from std_msgs.msg import Header
import math

rospy.init_node('converter')
pub = rospy.Publisher('joint_states', JointState)

msg_joint_states = JointState()
msg_joint_states.header = Header()
msg_joint_states.name = ['front_right_hinge_joint', 
                         'front_left_hinge_joint', 
                         'front_right_wheel_joint',
                         'front_left_wheel_joint', 
                         'rear_right_wheel_joint', 
                         'rear_left_wheel_joint']
msg_joint_states.velocity = []
msg_joint_states.effort = []

l_wheel, r_wheel = -3.14, -3.14


def callback(data):
    global msg_joint_states, l_wheel, r_wheel
    Angle = data.angle
    msg_joint_states.header.stamp = rospy.Time.now()
    steering = math.radians(Angle * 0.4)  # 20 / 50 = 0.4
    # print(steering, Angle * 0.4 * math.pi / 180, steering == Angle * 0.4 * math.pi / 180)

    if l_wheel > 3.14:
        l_wheel = -3.14
        r_wheel = -3.14
    else:
        l_wheel += 0.01
        r_wheel += 0.01

    msg_joint_states.position = [steering, 
                                 steering, 
                                 r_wheel, 
                                 l_wheel, 
                                 r_wheel,
                                 l_wheel]

    pub.publish(msg_joint_states)


rospy.Subscriber("motor", motor, callback)

rospy.spin()
