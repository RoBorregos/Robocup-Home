#!/usr/bin/env python

from gtts import gTTS
from io import BytesIO

from pygame import mixer
import pygame

from tempfile import TemporaryFile

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

# @@@@@@@@@@@@@@@@@@@@@@@@

###################################
# Funcionality is implemented here
###################################

def handle_voice_sythetizer(request_package):

	# Service has to return a response of the following class only.
	# meaningless values have been used to initialize objt. 
	# Modify only those filds that have a purpose on your service.
	response_package = home_std_srvResponse(1,[],0)
	
	print "Atending a request..."

	"""FUNCTIONALITY GOES HERE"""
	##########################################################################

	text_to_speak = request_package.textCommand

	tts = gTTS(text_to_speak, "en")

	sf = TemporaryFile()
	tts.write_to_fp(sf)
	sf.seek(0)
	mixer.init()
	mixer.music.load(sf)

	print "I will synthetize the following text : ", text_to_speak
	print "speaking now"
	mixer.music.play()

	# Wait to finish speaking
	while mixer.music.get_busy(): 
		pygame.time.Clock().tick(10)
	print "Done speaking"



	##########################################################################
	
	print "returing now"

	# This handle MUST return a Service Response 
	return response_package

def voice_sythetizer():
	rospy.init_node('voice_sythetizer_service_node')
	s = rospy.Service('voice_sythetizer', home_std_srv, handle_voice_sythetizer)
	
	print "########################################"
	print "   Voice Sythetizer is up and running."
	print "########################################"
	
	rospy.spin()

if __name__ == "__main__":
	voice_sythetizer()




