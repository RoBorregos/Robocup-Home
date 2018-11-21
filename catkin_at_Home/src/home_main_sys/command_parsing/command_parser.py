# Tokenizer and Parser to build gramatical rules and actions
import ply.lex as lex
import ply.yacc as yacc

import speech_recognition as sr
import time

# import pyttsx
# engine = pyttsx.init()

# Helper libraries to speak text
from gtts import gTTS
from io import BytesIO

from pygame import mixer
import pygame

from tempfile import TemporaryFile



debugg = False
####################################
#           Command Parser         #
####################################
import instructions_tokens
from instruction_map import *
lexer = lex.lex(module=instructions_tokens)


class command_parser():
	"""docstring for command_parser"""
	def __init__(self):
		self.command_in_text = ""


	def parse_command(self, command_string):
		print "string to decode a command, ", command_string
		command_detected = 0

		turn = False
		on = False
		off = False
		open_ = False
		close_ = False
		door = False

		ex = False
		faces = False
		dummy = False

		# look for tokens 
		lexer.input(command_string)
		for tok in lexer:
			
			if(tok.value == 'turn'):
				turn = True;
			elif(tok.value == 'on'):
				on = True
			elif(tok.value == 'off'):
				off = True
			elif(tok.value == 'open'):
				open_ = True
			elif(tok.value == 'close'):
				close_ = True
			elif(tok.value == 'door'):
				door = True
			elif(tok.value == 'execute'):
				ex = True
			elif(tok.value == 'faces'):
				faces = True
			elif(tok.value == 'dummy'):
				dummy = True

			print "VALUE OF CUR TOKEN IS, ", tok.value

		if(turn and on):
			command_detected = inst_turn_on
		elif(turn and off):
			command_detected = inst_turn_off
		elif(open_ and door):
			command_detected = inst_open_door
		elif(close_ and door):
			command_detected = inst_close_door
		elif(ex and faces):
			command_detected = inst_execute_faces
		elif(ex and dummy):
			command_detected = inst_execute_dummy

		print "COMANDO DE VOZ PARSEADO : ", command_detected

		
		return command_detected


	def audio_to_text(self):
		self.speak_text('Hello. What is your command')


		r = sr.Recognizer()
		with sr.Microphone() as source:
			print ('say something')
			audio = r.listen(source)

		# try:
		audio_string = r.recognize_google(audio)
		print(audio_string)
		# engine.say('I have the understand the following sentence.' + audio_string)
		# a = engine.runAndWait()
		# speak_text('I have the understand the following sentence.' + audio_string)
		self.speak_text('I have understand the following.')
		self.speak_text(audio_string)

		pass
		return audio_string
		# except:
		# 	print("Error parsing audio")
		# 	return ""
		# 	pass

	def speak_text(self, text):
		# text = "Hello world. Today will be a great day. Ingeniero Hinojosa is the best"
		tts = gTTS(text, "en")

		sf = TemporaryFile()
		tts.write_to_fp(sf)
		sf.seek(0)
		mixer.init()
		mixer.music.load(sf)
		mixer.music.play()

		# Wait to finish speaking
		while mixer.music.get_busy(): 
			pygame.time.Clock().tick(10)
			# a = raw_input()
		print "Done speaking"


if debugg:
	# create the command parser object
	command_object = command_parser()

	test = command_object.audio_to_text()
	decide = command_object.parse_command(test)
