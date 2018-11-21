#!/usr/bin/env python

import rospy
from home_main_sys.srv import *
import time
import requests
import serial
import subprocess

# @@@@@@@@@@@@@@@@@@@@@@@@

# SERVICE PKG DEFINITION
# 	works struct-like

# int8 debugMode					|
# string newFaceName				| Request params
# string textCommand				|
# ---
# int8 success	(1) TRUE (2) FALSE	|
# string[] facesDetected			| Response params
# int8 actionID						|

# @@@@@@@@@@@@@@@@@@@@@@@@

###################################
# Funcionality is implemented here
###################################

def handle_orb_movement_service(req):
	# Service has to return a response of the following class only.
	# meaningless values have been used to initialize objt. 
	# Modify only those filds that have a purpose on your service.
	response_package = home_std_srvResponse(1,[],0)
	
	print "Atending a request..."

	"""FUNCTIONALITY GOES HERE"""
	##########################################################################
	puerto = 'COM6'
	arduino = serial.Serial(puerto, 9600)
	print 'Connecting to ', puerto
	print 'Waiting for ROS command...'
	
	arduino.write("Init")
	arduino.write("1")

	subprocess.call(["Examples/Monocular/mono_tum","Vocabulary/ORBvoc.txt","Examples/Monocular/TUM1.yaml","Examples/Monocular/Sequence"])

	while arduino.in_waiting() <= 0:
		pass

	if arduino.read() == "0"
		print 'ORBSLAM2 done'

	##########################################################################
	
	print "returing now"

	# This handle MUST return a Service Response 
	return response_package

def atomic3_orb_movement():
	rospy.init_node('atomic3_orb_movement_service_node')
	s = rospy.Service('atomic3_orb_movement', home_std_srv, handle_orb_movement_service)
	
	print "########################################"
	print "Orb and Movement Service is up and running."
	print "########################################"
	
	rospy.spin()

if __name__ == "__main__":
	atomic3_orb_movement()