#!/usr/bin/env python

import sys
import rospy
from home_main_sys.srv import *
import time
# import home_std_srv.srv


# @@@@@@@@@@@@@@@@@@@@@@@@

# SERVICE PKG DEFINITION
# 	works struct-like

# int8 debugMode			
# string newFaceName		Request params
# string textCommand
# ---
# int8 success	(1) TRUE	(2) FALSE
# string[] facesDetected	Response params
# int8 actionID

# @@@@@@@@@@@@@@@@@@@@@@@@



# Service requieres a srv package
request_pakcage = [0, "Emilio is calling", "this is dummy command"]


def call_test_node_service(request_pakcage):
	print "waiting for the 3 services to be up"
	rospy.wait_for_service('atomic1_face_learning')
	rospy.wait_for_service('atomic2_face_detection')
	rospy.wait_for_service('atomic3_orb_movement')

	try:
		print "Generating Proxy caller objects"
		face_detection_service = rospy.ServiceProxy('atomic1_face_learning', home_std_srv)
		face_learning_service = rospy.ServiceProxy('atomic2_face_detection', home_std_srv)
		orb_movement_service = rospy.ServiceProxy('atomic3_orb_movement', home_std_srv)
		
		print "Caling face detection service now"
		t = time.time()
		response1 = face_learning_service(request_pakcage[0], request_pakcage[1], request_pakcage[2])
		print "Service has elapsed: ", time.time() - t, "\n"

		print "Caling face learning service now"
		t = time.time()
		response2 = face_detection_service(request_pakcage[0], request_pakcage[1], request_pakcage[2])
		print "Service has elapsed: ", time.time() - t, "\n"

		print "Caling orb movement service now"
		t = time.time()
		response3 = orb_movement_service(request_pakcage[0], request_pakcage[1], request_pakcage[2])
		print "Service has elapsed: ", time.time() - t, "\n"


		return (response1, response2, response3)

	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


if __name__ == "__main__":
	print "Calling services"
	response_array = call_test_node_service(request_pakcage)

	print response_array[0]
	print response_array[1]
	print response_array[2]