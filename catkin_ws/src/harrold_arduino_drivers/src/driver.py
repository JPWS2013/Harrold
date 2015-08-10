#!/usr/bin/env python


import serial
import rospy
from std_msgs.msg import String

class Arduino:

	def __init__(self, serial_port='/dev/ttyACM0', baudrate=115200):
		self.port=serial_port
		self.baud=baudrate
		self.ser_obj=serial.Serial(self.port, self.baud, timeout=1)
		self.pub = rospy.Publisher('arduino_test', String, queue_size=10)

		self.run_arduino()

	def run_arduino(self):

		rospy.init_node('arduino_driver', anonymous=False)
		print "Arduino Driver is Running!"

		while not rospy.is_shutdown():

			message=self.ser_obj.readline()
			result=message.strip().split(',')

			if len(result)==7:

## TODO: The stuff below this line needs to be written such that it publishes to the /imu/data topic 
#        in a manner that is appropriate for what that topic expects to see (see ROS documentation)

				accel=result[0:3]
				gyro=result[3:6]
				batt=result[6]

				res=[accel, gyro, batt]

				self.pub.publish(message)

				#print 'Accel=', accel
				#print 'Gyro=', gyro
				#print 'Batt=', batt
				#print ''

if __name__ == '__main__':
    try:
        Arduino()
    except rospy.ROSInterruptException:
        pass