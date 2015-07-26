   1 #! /usr/bin/env python
   2 # license removed for brevity

   3 import rospy
   4 from std_msgs.msg import String
   5 
   6 def talker():
   7     pub = rospy.Publisher('Hello_World', String, queue_size=10)
   8     rospy.init_node('talker', anonymous=True)
   9     rate = rospy.Rate(10) 
