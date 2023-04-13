#!/usr/bin/env python
import serial, rospy, time
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
import tf


lidar_points = None
def lidar_callback(msg):
	global lidar_points
	print(len(msg.ranges))
	lidar_points = msg.ranges

rospy.init_node('lidar')
rospy.Subscriber("/scan", LaserScan, lidar_callback, queue_size=1)

pub1 = rospy.Publisher('scan1', Range, queue_size = 10)
pub2 = rospy.Publisher('scan2', Range, queue_size = 10)
pub3 = rospy.Publisher('scan3', Range, queue_size = 10)
pub4 = rospy.Publisher('scan4', Range, queue_size = 10)

broadcaster = tf.TransformBroadcaster()
quat = tf.transformations.quaternion_from_euler(0, 0, 0)


msg_range = Range() 
msg_header = Header()

msg_range.radiation_type = Range().ULTRASOUND
msg_range.min_range = 0.02
msg_range.max_range = 2.0 #float("inf")
msg_range.field_of_view = (30.0/180.0)*3.14

while not rospy.is_shutdown():
	if lidar_points == None:
		continue

	msg_header.frame_id = 'front'
	msg_range.header = msg_header
	msg_range.range = lidar_points[90]
	pub1.publish(msg_range)

	msg_header.frame_id = 'right'
	msg_range.header = msg_header
	msg_range.range = lidar_points[180]
	pub2.publish(msg_range)

	msg_header.frame_id = 'back'
	msg_range.header = msg_header
	msg_range.range = lidar_points[270]
	pub3.publish(msg_range)

	msg_header.frame_id = 'left'
	msg_range.header = msg_header
	msg_range.range = lidar_points[0]
	pub4.publish(msg_range)

	broadcaster.sendTransform(
	(0, 0, 0.),
	quat,
	rospy.Time.now(),
	"base_link",
	"odom")

	time.sleep(0.5)
