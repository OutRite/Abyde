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

def abyde_multiply(num, times, outvar):
	output_prg = '||'
	output_prg += 'm ro {}|'.format(num) # we move the number into ro
	output_prg += 'm rt ro|' # we move ro into rt
	output_prg += 'm ra {}||'.format(int(times)-1) # we move the iteration count into ra
	output_prg += 'b ra|' # we check if we've gone through all iterations
	output_prg += 'a ro rt|' # we haven't, so we add ro and the first number
	output_prg += 'm rb ro|' # we move ro into rb
	output_prg += 's ra 1|' # we decrease the iteration count
	output_prg += 'm ra ro|' # we move everything back into normal positions
	output_prg += 'm ro rb|' # and now ro contains our new number
	output_prg += 'r||' # repeat until done
	output_prg += 'm {} ro|'.format(outvar) # we move our new number into whatever variable provided
	return output_prg



for i in range(len(commands)):
	current_command = commands[i].split(' ')
	if current_command[0] == 'print':
		compiled_prg += abyde_print(commands[i][6:])
	elif current_command[0] == 'exit':
		compiled_prg += 'q|'
	elif current_command[0] == 'add':
		compiled_prg += 'a '
		compiled_prg += current_command[1]
		compiled_prg += ' '
		compiled_prg += current_command[3]
		compiled_prg += '|'
		compiled_prg += 'm {} ro|'.format(current_command[5]) 
	elif current_command[0] == 'sub':
		compiled_prg += 's '
		compiled_prg += current_command[1]
		compiled_prg += ' '
		compiled_prg += current_command[3]
		compiled_prg += '|m {} ro|'.format(current_command[5])
	elif current_command[0] == 'display':
		compiled_prg += 'm rs {}|o|'.format(current_command[1])
	elif current_command[0] == 'notzero':
		compiled_prg += 'b {}|'.format(current_command[1])
	elif current_command[0] == 'endif':
		compiled_prg += '||'
	elif current_command[0] == 'set':
		compiled_prg += 'm {} {}|'.format(current_command[1], current_command[3])
	elif current_command[0] == 'input':
		compiled_prg += 'i|m {} ro|'.format(current_command[2])
	elif current_command[0] == 'multiply':
		compiled_prg += abyde_multiply(current_command[1], current_command[3], current_command[5])
	else:
		print("ERROR: INVALID COMMAND")
		print(commands[i])

compiled_prg += 'q'

print(compiled_prg)