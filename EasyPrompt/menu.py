# EasyPrompt Menu
# by Evan Parker (@evprkr)
# https://github.com/evprkr/EasyPrompt

# Features to add

# Known bugs

import inspect, shlex

class Menu:
	def __init__(self, prompt=None, newline=None, items=None)
		if prompt == None: self.prompt == '> '
		else self.prompt == prompt

		self.newline = newline
		self.items = []

	def add_item(self, name, callback, args=None):
		item = [name, callback, args]
		self.items.append(item)

	def get_selection(self):
		selection = input(self.prompt)
