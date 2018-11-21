#!/usr/bin/env python
# -- coding: utf-8 --
# Para que entienda acentos

# Speech to text converter
import speech_recognition as sr

# ROS 
import rospy
from std_msgs.msg import String

"""
VALID STATED FOR THE VOICE CONTROLLED STATE MACHINE
"""
# To do:
# 	- Make readonly variables
class vcsm_STATE(object):
	def __init__(self):
		# A voice controlled state machine will begin in this state
		self.neutral_state = "neutral_state"
		
		# Stand by state for polling process
		self.stand_by = "stand_by"
		
		# decofing_voice (Speech-To-Text)
		self.decofing_voice = "decofing_voice"
		
		# Waiting for asignation
		self.waiting_for_asignation = "waiting_for_asignation"

		# Asignation in progress
		self.asignation_in_progress = "asignation_in_progress"
		
		# Parsing command
		self.parsing_command = "parsing_command"

		# Talk to module 1
		self.talk_to_module1 = "talk_to_module1"

"""
FUNCTIONS AND TRANSITIONS FOR THE VOICE CONTROLLED STATE MACHINE
"""	
class voice_controlled_state_machine():
	"""docstring for voice_controlled_state_machine"""

	def __init__(self):
		self.current_state = vcsm_STATE().neutral_state
		self.target_state = vcsm_STATE().neutral_state

	"""
	PROCESS STATE TRANSITION
	"""

	# Process method to reach target state
	def process_state(self, debug=False):

		possible_roll_back_state = self.current_state

		if debug:
			print "Processing from " + self.current_state + " to: " + self.target_state

		# From stand by to 
		if self.target_state == vcsm_STATE().waiting_for_asignation:
			self.process_assignation()


	"""
	TRANSITION METHODS
	"""

	# Reach waiting for asignation state
	def process_assignation(self):
		# From stand by to waiting for assignation
		if self.current_state == vcsm_STATE().stand_by:
			try:
				######
				# TODO:
				# Shell to implement method to initialice stuff(ROS)
				#####
				print "hola"
				self.current_state = vcsm_STATE().waiting_for_asignation
				self.target_state = vcsm_STATE().asignation_in_progress
				pass
			except:
				pass

	def message_to_module1(self, message_str):
		if not rospy.is_shutdown():
			pub = rospy.Publisher('chatter', String, queue_size=10)
			rospy.init_node('talker', anonymous=True)
			rate = rospy.Rate(10) # 10hz
			# while not rospy.is_shutdown():
			rospy.loginfo(message_str)
			pub.publish(message_str)
			rate.sleep()

	def message_to_module2(self, message_str):
		if not rospy.is_shutdown():
			pub = rospy.Publisher('chatter2', String, queue_size=10)
			rospy.init_node('talker2', anonymous=True)
			rate = rospy.Rate(10) # 10hz
			# while not rospy.is_shutdown():
			rospy.loginfo(message_str)
			pub.publish(message_str)
			rate.sleep()

