#!/usr/bin/env python

import rospy, math, rospkg
from sensor_msgs.msg import Imu

from tf.transformations import quaternion_from_euler

imu_msg = Imu()
imu_msg.header.frame_id = 'map'
degree2rad = float(math.pi)/float(180.0)
rad2degree = float(180.0)/float(math.pi)

rospy.init_node("imu_generator")
pub=rospy.Publisher('imu', Imu, queue_size=1)

path = rospkg.RosPack().get_path('rviz_imu')+"/src/imu_data.txt"

rate = rospy.Rate(10)
with open(path, 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    roll, pitch, yaw = map(float, line.replace(' :', '').replace(',', '').split(' ')[1::2])
    
    x, y, z, w = quaternion_from_euler(roll, pitch, yaw)
    imu_msg.orientation.x, \
    imu_msg.orientation.y, \
    imu_msg.orientation.z, \
    imu_msg.orientation.w = x, y, z, w

    imu_msg.header.stamp = rospy.Time.now()
    imu_msg.header.seq = idx
    pub.publish(imu_msg)
    print(imu_msg)
    rate.sleep()


    