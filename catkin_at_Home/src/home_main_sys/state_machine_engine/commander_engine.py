#!/usr/bin/env python
# -- coding: utf-8 --
# Para que entienda acentos


"""
Provitional feature switches
"""
debug = True

# Speech to text converter
import speech_recognition as sr

# State machine for the voice controller
from voice_controlled_state_machine import vcsm_STATE, voice_controlled_state_machine

# text-to-command parser
from command_parser import command_parser

from instruction_map import *

# create the command parser object
command_object = command_parser()

# creating the state machine object
engine = voice_controlled_state_machine()
# Activate the engine to asign a further state
engine.current_state = vcsm_STATE().stand_by
engine.target_state = vcsm_STATE().waiting_for_asignation




while True:
	try:
		# process the current state to target state
		# engine.process_state(debug)
		print "calling audio listener"
		test = command_object.audio_to_text()
		decide = command_object.parse_command(test)
		print "------------------------------------------------"

		print "Hello"
		if decide == inst_execute_faces:
			print "calling modulo de faces"
			engine.message_to_module1("llamando al modulo de caras")
		elif decide == inst_execute_dummy:
			engine.message_to_module2("llamando a otro modulo dummy")

		print "decide: ", decide

		if test == "quit":
			break

	except:
		# To do, loop for failback support
		print "Exception ocurred, rolling back to stand by state"
		print "Rolling back NOT IMPLEMENTED"
		pass


