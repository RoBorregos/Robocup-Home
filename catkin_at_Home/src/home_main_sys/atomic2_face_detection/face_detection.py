#!/usr/bin/env python

import rospy
from home_main_sys.srv import *
import time

###################################
# Funcionality is implemented here
###################################

def handle_face_detection_service(req):
	print "Atending a request... sleeping 5 sec"
	time.sleep(5)
	print "returing now"

	# This handle MUST return a Service Response 
	return home_std_srvResponse(req.debugMode, [req.newFaceName])

def atomic2_face_detection():
	rospy.init_node('atomic2_face_detection_service_node')
	s = rospy.Service('atomic2_face_detection', home_std_srv, handle_face_detection_service)
	
	print "########################################"
	print "Face Detection Service is up and running."
	print "########################################"
	rospy.spin()

if __name__ == "__main__":
	atomic2_face_detection()