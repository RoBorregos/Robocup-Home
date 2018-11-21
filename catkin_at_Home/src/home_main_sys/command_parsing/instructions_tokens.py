####################################
#           Command Tokens        #
####################################
tokens = [
	'EXECUTE',

	'FACES',

	'DUMMY',
	'TURN',
	'ON',
	'OFF',
	'LIGHT',

	'CLOSE',
	'OPEN',
	'DOOR' 

]
t_TURN = r'turn'
t_ON = r'on'
t_OFF = r'off'
t_CLOSE = r'close'
t_OPEN = r'open'
t_DOOR = r'door'
t_EXECUTE = r'execute'
t_FACES = 'faces'
t_DUMMY = 'dummy'

def t_error(t):
	t.lexer.skip(1)
