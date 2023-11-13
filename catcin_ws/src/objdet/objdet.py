#!/usr/bin/env python3
import rospy  # Import the ROS Python library
from sensor_msgs.msg import Image  # Import the Image message type from ROS
from cv_bridge import CvBridge  # Import CvBridge for converting between ROS Image and OpenCV
from ultralytics import YOLO  # Import the YOLO model from Ultralytics
import cv2  # Import the OpenCV library

# Define a class called RosNode
class RosNode:
    def __init__(self):
        # Initialize the ROS node with the name "ros_node"
        rospy.init_node("ros_node")
        # Log an informational message indicating the node has started
        rospy.loginfo("Starting RosNode.")
        # Subscribe to the "/usb_cam/image_raw" topic and call self.img_callback when a message is received
        rospy.Subscriber("/usb_cam/image_raw", Image, self.img_callback)
        # Create a ROS publisher to publish annotated images to the "/cvimg" topic
        self.cvimg_pub = rospy.Publisher("/cvimg", Image, queue_size=10)
        pass  # Placeholder, no additional initialization code here

    # Define a callback function for processing image messages
    def img_callback(self, msg):
        if (msg):  # Check if the message is not empty
            bridge = CvBridge()  # Create a CvBridge instance for image conversion
            # Convert the ROS Image message to an OpenCV image with the specified encoding
            cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            print(cv_image)  # Print the OpenCV image (for debugging)
            # Create a YOLO model instance with the specified weights file
            model = YOLO('/home/student/Downloads/yolov8n.pt')
            # Perform object detection on the input image using YOLO
            result = model(cv_image)
            # Generate an annotated frame with detected objects and draw bounding boxes
            annotadet_frame = result[0].plot()
            # Convert the annotated frame back to a ROS Image message
            msg_to_img = bridge.cv2_to_imgmsg(annotadet_frame)
            # Publish the annotated image to the "/cvimg" topic
            self.cvimg_pub.publish(msg_to_img)

# Check if the script is being run as the main program
if __name__ == "__main__":
    ros_node = RosNode()  # Create an instance of the RosNode class
    rospy.spin()  # Start the ROS node and wait for messages

