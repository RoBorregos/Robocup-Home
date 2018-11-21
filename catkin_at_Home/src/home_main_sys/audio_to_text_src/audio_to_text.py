#!/usr/bin/env python


# Speech to text converter
import speech_recognition as sr

import sys
import rospy
from home_main_sys.srv import *
import time

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
# string textFromAudio

# @@@@@@@@@@@@@@@@@@@@@@@@

###################################
# Funcionality is implemented here
###################################

def handle_audio_to_text(request_package):

	# Service has to return a response of the following class only.
	# meaningless values have been used to initialize objt. 
	# Modify only those filds that have a purpose on your service.
	response_package = home_std_srvResponse(1,[],"",0,"")
	
	print "Atending a request..."

	"""FUNCTIONALITY GOES HERE"""
	##########################################################################
	flag = False
	
	while not flag:
		try:

			r = sr.Recognizer()
			with sr.Microphone() as source:
				print ('say something')
				audio = r.listen(source)

			audio_string = r.recognize_google(audio)
			print(audio_string)

			response_package.textFromAudio = audio_string
			##########################################################################
			
			print "returing now"

			flag = True
			# This handle MUST return a Service Response 
			return response_package
		except:
			print "An Exception has ocurred."
			flag = False

def audio_to_text():
	rospy.init_node('audio_to_text_service_node')
	s = rospy.Service('audio_to_text', home_std_srv, handle_audio_to_text)
	
	print "########################################"
	print "   Audio to text Service is up and running."
	print "########################################"
	
	rospy.spin()

if __name__ == "__main__":
	audio_to_text()




		
