#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys


def move_circle_turtle(linear_velocity1, angular_velocity1):
	rospy.init_node('turtlemove', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)

	vel = Twist()

	while True:

		vel.linear.x = linear_velocity1
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = angular_velocity1

		pub.publish(vel)
		rate.sleep()

move_circle_turtle(9,4)

		


