#!/usr/bin/env python

import rospy
from home_main_sys.srv import *
import time
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


def handle_face_learning_service(request_package):
	# Service has to return a response of the following class only.
	# meaningless values have been used to initialize objt. 
	# Modify only those filds that have a purpose on your service.
	response_package = home_std_srvResponse(1,[],0)
	
	print "Atending a request..."

	"""FUNCTIONALITY GOES HERE"""
	##########################################################################
	# time.sleep(5)
	newName = request_package.newFaceName
	subprocess.call("python3","/home/sebasrivera96/Documents/Github/tabellarius/main.py", "learn", newName])



	##########################################################################
	
	print "returing now"

	# This handle MUST return a Service Response 
	return response_package

def atomic1_face_learning():
	rospy.init_node('atomic1_face_learning_service_node')
	s = rospy.Service('atomic1_face_learning', home_std_srv, handle_face_learning_service)

	print "########################################"
	print "Face Learning Service is up and running."
	print "########################################"

	rospy.spin()

if __name__ == "__main__":
	atomic1_face_learning()