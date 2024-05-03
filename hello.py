#! /usr/bin/env python3

"""
Python 版 HelloWorld

"""
import rospy
import mmap
import time
from std_msgs.msg import Float64MultiArray

if __name__ == "__main__":
        rospy.init_node('data_pub',anonymous=True)
        pub=rospy.Publisher('pose_data',Float64MultiArray,queue_size=10)
        rate=rospy.Rate(1)
        while not rospy.is_shutdown():
                with open("shared_memory.txt","r") as f:
                        data=f.read().strip()
                        rows=data[2:-2].split("]\n [")
                        array=[[float(num) for num in row.split()]for row in rows]

                        print(array)
                        array_msg=Float64MultiArray()
                        array_msg.data=[num for sublist in array for num in sublist]
                        pub.publish(array_msg)
                rate.sleep()