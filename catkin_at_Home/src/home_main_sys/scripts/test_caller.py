#!/usr/bin/env python

import sys
import rospy
from home_main_sys.srv import *
import time
# import home_std_srv.srv

# Service requieres a srv package
srv_pack = [0, "Emilio is calling"]


def call_test_node_service(srv_pack):
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
		response1 = face_learning_service(srv_pack[0], srv_pack[1])
		print "Service has elapsed: ", time.time() - t, "\n"

		print "Caling face learning service now"
		t = time.time()
		response2 = face_detection_service(srv_pack[0], srv_pack[1])
		print "Service has elapsed: ", time.time() - t, "\n"

		print "Caling orb movement service now"
		t = time.time()
		response3 = orb_movement_service(srv_pack[0], srv_pack[1])
		print "Service has elapsed: ", time.time() - t, "\n"


		return (response1, response2, response3)

	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


if __name__ == "__main__":
	print "Calling services"
	response_array = call_test_node_service(srv_pack)

	print response_array[0]
	print response_array[1]
	print response_array[2]