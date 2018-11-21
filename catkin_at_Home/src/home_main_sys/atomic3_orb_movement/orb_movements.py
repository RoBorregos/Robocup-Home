#!/usr/bin/env python

import rospy
from home_main_sys.srv import *
import time

###################################
# Funcionality is implemented here
###################################

def handle_orb_movement_service(req):
	print "Atending a request... sleeping 5 sec"
	time.sleep(5)
	print "returing now"

	# This handle MUST return a Service Response 
	return home_std_srvResponse(req.debugMode, [req.newFaceName])

def atomic3_orb_movement():
	rospy.init_node('atomic3_orb_movement_service_node')
	s = rospy.Service('atomic3_orb_movement', home_std_srv, handle_orb_movement_service)
	
	print "########################################"
	print "Orb and Movement Service is up and running."
	print "########################################"
	
	rospy.spin()

if __name__ == "__main__":
	atomic3_orb_movement()