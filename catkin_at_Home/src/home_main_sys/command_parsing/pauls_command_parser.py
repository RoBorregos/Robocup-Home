#!/usr/bin/env python

import rospy
from home_main_sys.srv import *
import time
import subprocess
import os


# @@@@@@@@@@@@@@@@@@@@@@@@

# SERVICE PKG DEFINITION
# 	works struct-like

# int8 debugMode					|
# string newFaceName				| Request params
# string textCommand				|
# ---
# int8 success	(1) TRUE (2) FALSE	|
# string[] facesDetected			| Response params
# string targetFaceName				|
# int8 actionID						|
# string textFromAudio

# @@@@@@@@@@@@@@@@@@@@@@@@

###################################
# Funcionality is implemented here
###################################

def handle_command_parsing(request_package):
	# Service has to return a response of the following class only.
	# meaningless values have been used to initialize objt. 
	# Modify only those filds that have a purpose on your service.
	response_package = home_std_srvResponse(1,[],"",0,"")
	
	print "Atending a request..."

	"""FUNCTIONALITY GOES HERE"""
	##########################################################################
	command_in_text = request_package.textCommand
	response_package.actionID = -1
	response_package.targetFaceName = ""

	f = open('sentence.txt', 'w')
	f.write(command_in_text)
	#Call compiled parser
	dir_path = os.path.dirname(os.path.realpath(__file__))
	#print (dir_path)
	loc = dir_path+'/main'
	#print(loc)
	p = subprocess.Popen([loc])
	print(p)
	out = open('output.txt','r+')
	answer = out.readline()
	params = []
	for word in answer.split():
        	params.append(word)      
	print(params)
	if(params[0]!=-1 and params[0]!=4):
		response_package.actionID = params[0]
	if(len(params)>1):
		response_package.targetFaceName = params[1]
	
	out.close()
	os.remove('output.txt')


	##########################################################################
	
	print "returing now"

	# This handle MUST return a Service Response 
	return response_package

def command_parsing():
	rospy.init_node('command_parsing_service_node')
	s = rospy.Service('command_parsing', home_std_srv, handle_command_parsing)

	print "########################################"
	print "Command Parsing Service is up and running."
	print "########################################"

	rospy.spin()

if __name__ == "__main__":
	command_parsing()