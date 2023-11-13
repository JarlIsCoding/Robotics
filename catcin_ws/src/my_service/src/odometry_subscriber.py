#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point

# Global variables to store the position and orientation
position_x = 0.0
position_y = 0.0
position_z = 0.0
orientation_w = 0.0

# Global variables to store the goal point
goal_x = 0.0
goal_y = 0.0
goal_z = 0.0

def odom_callback(data):
    # Callback function to handle received odometry messages
    global position_x, position_y, position_z, orientation_w

    # Store the position and orientation
    position_x = data.pose.pose.position.x
    position_y = data.pose.pose.position.y
    position_z = data.pose.pose.position.z
    orientation_w = data.pose.pose.orientation.w

    rospy.loginfo("Received Odometry Data: "
                  "Position (x, y, z): (%f, %f, %f), Orientation (w): %f",
                  position_x, position_y, position_z, orientation_w)

def goal_callback(data):
    # Callback function to handle received goal point messages
    global goal_x, goal_y, goal_z

    # Store the goal point
    goal_x = data.x
    goal_y = data.y
    goal_z = data.z

    rospy.loginfo("Received Goal Point: (x, y, z): (%f, %f, %f)",
                  goal_x, goal_y, goal_z)

def main():
    rospy.init_node('odometry_goal_subscriber', anonymous=True)

    # Set the rate to 5 Hz
    rate = rospy.Rate(5)

    # Subscribe to the '/ground_truth/state' odometry topic
    rospy.Subscriber('/ground_truth/state', Odometry, odom_callback)

    # Subscribe to the '/goal' topic with Point message type
    rospy.Subscriber('/goal', Point, goal_callback)

    while not rospy.is_shutdown():
        # Perform other processing here if needed

        rate.sleep()

if __name__ == '__main__':
    main()
