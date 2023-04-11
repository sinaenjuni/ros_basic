#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import time

rospy.init_node('timeslot_sender_node', anonymous=True)
pub = rospy.Publisher('timeslot_topic', Int32, queue_size=1)

rate = rospy.Rate(5)
def pub_count(count):
    for n in range(0, count):
        pub.publish(n)


while not rospy.is_shutdown():
    count = input("count: ")
    rate.sleep()

    total_time = time.time()

    for _ in range(0, 5):
        start_pub_time = time.time()
        pub_count(count)
        end_pub_time = time.time()
    
        rate.sleep()
        end_sleep_time = time.time()

        print(("pub_time: ",
              round(end_pub_time - start_pub_time, 4), 
              "sleep_time: ",
              round(end_sleep_time - end_pub_time, 4)))
        
    print("total: ", round(time.time() - total_time, 4))