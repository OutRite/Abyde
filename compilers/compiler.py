#AbydeScript to Abyde compiler.
import sys

if len(sys.argv) < 2:
	print("Usage: ./compiler.py [program.as]")
	sys.exit()

as_file = open(sys.argv[1])

as_prg = as_file.read()

as_file.close()

as_prg = as_prg.replace('\r', '') #augh windows i hate you

commands = as_prg.split('\n')

compiled_prg = ''

def abyde_print(text):
	text_ints = list(text)
	for i in range(len(text_ints)):
		if text_ints[i] == '`':
			text_ints[i] = ord('\n')
		else:
			text_ints[i] = ord(text_ints[i])
	output_prg = ''
	for j in range(len(text_ints)):
		output_prg += 'm rs {}|o|'.format(text_ints[j])
	return output_prg




for i in range(len(commands)):
	if commands[i].split(' ')[0] == 'print':
		compiled_prg += abyde_print(commands[i][6:])
	elif commands[i].split(' ')[0] == 'exit':
		compiled_prg += 'q|'
	elif commands[i].split(' ')[0] == 'add':
		compiled_prg += 'a '
		compiled_prg += commands[i].split(' ')[1]
		compiled_prg += ' '
		compiled_prg += commands[i].split(' ')[3]
		compiled_prg += '|'
		compiled_prg += 'm ro {}|'.format(commands[i].split(' ')[5]) 
	elif commands[i].split(' ')[0] == 'display':
		compiled_prg += 'm rs {}|o|'.format(commands[i].split(' ')[1])
	else:
		print("ERROR: INVALID COMMAND")
		print(commands[i])

compiled_prg += 'q'

print(compiled_prg)