#!/usr/bin/env python


# Speech to text converter
import speech_recognition as sr

import sys
import rospy
from home_main_sys.srv import *
import time

def call_test_node_service(debuging, newFaceName):
	rospy.wait_for_service('test_node_service')
	try:
		testNodeObjectResponse = rospy.ServiceProxy('test_node_service', home_std_srv)
		print "Calind service now"
		t = time.time()
		response = testNodeObjectResponse(debuging, newFaceName)
		print "Service has elapsed: ", time.time() - t
		return (response.success, response.facesDetected)
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


if __name__ == "__main__":
	print "Calling Test Node Service"
	print call_test_node_service(0,"emiliooo")