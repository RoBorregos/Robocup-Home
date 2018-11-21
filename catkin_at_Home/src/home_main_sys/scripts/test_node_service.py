#!/usr/bin/env python

# from home_main_sys.srv import *


import rospy
from home_main_sys.srv import *
import time


# Funcionality is implemented here
def handle_test_node_service(req):
	print "Atending a request... sleeping 10 sec"
	time.sleep(10)
	print "returing now"
	return home_std_srvResponse(req.debugMode, [req.newFaceName])

def test_node_service():
	rospy.init_node('test_node_service_node')
	s = rospy.Service('test_node_service', home_std_srv, handle_test_node_service)
	print "Home Service is up and running."
	rospy.spin()

if __name__ == "__main__":
	test_node_service()