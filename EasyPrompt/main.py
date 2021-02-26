# EasyPrompt v0.1.8
# by Evan Parker (@evprkr)
# https://github.com/evprkr/EasyPrompt

# Features to add
# * Specify allowed argument types for commands, special error for "expected string, got integer"
# * 'get_selection' function for displaying a list of options and taking input to trigger specific callbacks

# Known bugs
# * 'get_input' always returns 'None', should fix it to return the return value of the callback function
# * Entering a blank command does the big kill

import inspect, shlex

# Main Commander Class
class Commander:
	def __init__(self, prompt=None, newline=True, commands=None, previous_cmd=None):
		if prompt == None: self.prompt = '> '
		else: self.prompt = prompt

		self.newline = newline
		self.commands = []
		self.previous_cmd = previous_cmd

	def get_input(self, prompt=None):
		if prompt is None: prompt = self.prompt

		cmd_input = input(prompt)

		if cmd_input == '!!':
			if self.previous_cmd != None:
				self.parse_command(self.previous_cmd)
			else:
				print("Error: no command history")
		else:
			self.parse_command(cmd_input)

	def parse_command(self, cmd_input):
		self.previous_cmd = cmd_input
		input_split = shlex.split(cmd_input)

		for command in self.commands:
			if input_split[0] in command:
				callback = command[1]
				arg_num = len(inspect.getfullargspec(command[1]).args)

				if len(input_split)-1 != arg_num:
					print(f'Error: expected {arg_num} arguments, got {len(input_split)-1}')
					if self.newline == True: print('')
					return

				if len(input_split) > 1:
					cmd_args = []
					for i in range(1, arg_num+1):
						cmd_args.append(input_split[i])

					callback(*cmd_args)
					if self.newline == True: print('')
					return

				callback()
				if self.newline == True: print('')
				return
		else:
			print(f"Command not found: '{input_split[0]}'")
			if self.newline == True: print('')

	def add_command(self, trigger, callback, args=None):
	   command = [trigger, callback, args]
	   self.commands.append(command)

# testing
def dongus(): print('dongus')

prompt = Commander(newline=False)
prompt.add_command('dingus', dongus)

while True:
	prompt.get_input()
