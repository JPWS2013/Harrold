#!/usr/bin/env python


import serial
import rospy
from std_msgs.msg import String, Float64
from sensor_msgs.msg import Imu

class Arduino:

	def __init__(self, serial_port='/dev/ttyACM0', baudrate=115200):
		self.port=serial_port
		self.baud=baudrate
		self.ser_obj=serial.Serial(self.port, self.baud, timeout=1)
		self.imu_pub = rospy.Publisher('/mobile_base/sensors/imu_data', Imu, queue_size=10)
		self.batt_pub = rospy.Publisher('/robot_batt', Float64, queue_size=10)

		self.run_arduino()

	def run_arduino(self):

		rospy.init_node('arduino_driver', anonymous=False)
		print "Arduino Driver is Running!"

		while not rospy.is_shutdown():

			message=self.ser_obj.readline()
			result=message.strip().split(',')

			if len(result)==7:

				imu_message=Imu()

				imu_message.header.stamp=rospy.Time.now()
				imu_message.header.frame_id="/imu"

				imu_message.orientation_covariance=[-1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

				imu_message.linear_acceleration.x=float(result[0])
				imu_message.linear_acceleration.y=float(result[1])
				imu_message.linear_acceleration.z=float(result[2])

				imu_message.angular_velocity.x=float(result[3])
				imu_message.angular_velocity.y=float(result[4])
				imu_message.angular_velocity.z=float(result[5])

				# accel=result[0:3]
				# gyro=result[3:6]
				# batt=result[6]

				#res=[accel, gyro, batt]

				# self.imu_pub.publish(imu_message)
				self.imu_pub.publish(imu_message)
				self.batt_pub.publish(float(result[6]))


if __name__ == '__main__':
	try:
		Arduino()

	except rospy.ROSInterruptException:
		pass