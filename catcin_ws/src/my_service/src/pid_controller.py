#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point

# Global variables for current position, goal position, and control command
current_position = Point()
goal_position = Point()
control_command = Twist()

# PID controller gains
kp = 0.5  # Proportional gain
ki = 0.0  # Integral gain
kd = 0.0  # Derivative gain

# Previous error for derivative control
previous_error = Point()  # Initialize previous_error here

def odom_callback(data):
    # Callback function to update the current position from the odometry
    global current_position
    current_position = data.pose.pose.position

def goal_callback(data):
    # Callback function to update the goal position
    global goal_position
    goal_position = data

def pid_controller():
    global previous_error  # Declare previous_error as global

    # Initialize the ROS node
    rospy.init_node('pid_controller', anonymous=True)

    # Create subscribers for odometry and goal topics
    rospy.Subscriber('/ground_truth/state', Odometry, odom_callback)
    rospy.Subscriber('/goal', Point, goal_callback)

    # Create a publisher for control commands (/cmd_vel)
    control_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Create a rate object to control the PID loop frequency (adjust as needed)
    rate = rospy.Rate(5)  # 5 Hz

    while not rospy.is_shutdown():
        # Calculate the error between current and goal position
        error = Point()
        error.x = goal_position.x - current_position.x
        error.y = goal_position.y - current_position.y
        error.z = goal_position.z - current_position.z

        # PID control algorithm
        control_command.linear.x = kp * error.x + ki * error.x + kd * (error.x - previous_error.x)
        control_command.linear.y = kp * error.y + ki * error.y + kd * (error.y - previous_error.y)
        control_command.linear.z = kp * error.z + ki * error.z + kd * (error.z - previous_error.z)

        # Publish the control command
        control_publisher.publish(control_command)

        # Store the current error for the next iteration
        previous_error = error

        rate.sleep()

if __name__ == '__main__':
    try:
        pid_controller()
    except rospy.ROSInterruptException:
        pass
