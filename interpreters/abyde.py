# imports
import sys

# check for file

if len(sys.argv) < 2:
	print("Usage: ./abyde.py [program name.abyde]")
	sys.exit()

# read program

abyde_file = open(sys.argv[1])
abyde_prg = abyde_file.read()
abyde_file.close()

# split sections into array

sections = abyde_prg.split("||")

# split commands into array, in each section

for i in range(len(sections)):
	sections[i] = sections[i].split("|")

# start execution

current_section = 0

on_repeat = False

register_names = ['ro', 'ra', 'rb', 'rs']

ro = 0
ra = 0
rb = 1
rs = 0
rt = 0

while True:
	for i in range(len(sections[current_section])):
		on_repeat = False
		current_command = sections[current_section][i]
		# print(current_command)
		# print('ra: {} rb: {} ro: {} rs: {} rt: {}'.format(ra,rb,ro,rs,rt))
		current_command = current_command.split(' ')
		if current_command[0] == 'a':
			exec('ro = {} + {}'.format(current_command[1], current_command[2]))
		elif current_command[0] == 's':
			exec('ro = {} - {}'.format(current_command[1], current_command[2]))
		elif current_command[0] == 'm':
			exec('{} = {}'.format(current_command[1], current_command[2]))
		elif current_command[0] == 'o':
			print(chr(rs), end='')
		elif current_command[0] == 'i':
			ro = ord(list(input(''))[0])
		elif current_command[0] == 'r':
			on_repeat = True
			break
		elif current_command[0] == 'b':
			if eval(current_command[1]) == 0:
				break
		elif current_command[0] == 'q':
			sys.exit()
		else:
			print('', end='') # basic nop, we assume this is some sort of data/invalid command
	if on_repeat is False:
		current_section += 1
	# print('DEBUG: current_section = ' + str(current_section))
