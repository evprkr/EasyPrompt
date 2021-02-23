# EasyPrompt
Simple module for taking and parsing commands from the user in a prompt-style interface

### Installation
Install using ``pip`` or ``pip3`` like any other package

    pip install easyprompt

Then just import it as you normally would

	import EasyPrompt

### Usage
First, you have to set up the main Commander class.

	CommanderName = EasyPrompt.Commander()

After that, all you have to do is add commands to the prompt...

	CommanderName.add_command('hello', hello_func)

Then start the prompt!

	CommanderName.get_input()

And that's it. After calling ``get_input()`` you'll be greeted with a prompt, featuring whatever you set your prompt to be, or the default '> ' prompt.
Errors are given when a command doesn't exist or if too many or too few arguments are passed. I recommend sticking your ``get_input()`` in a while loop, so it will keep prompting the user until it gets the input it needs.

There's also a built-in function for repeating the last entered command, which is triggered with ``!!``

### More Detail
* *Commander* - Usage: ``CommanderName = EasyPrompt.Commander(prompt)`` This is the class that holds all of your commands. You can have multiple Commander classes to hold different sets of commands, so that certain parts of your program only accept certain commands. You can also set ``prompt`` to whatever text you want to be displayed on the prompt, or leave it empty to get the default, which is ``> ``
* *add_command* - Usage: ``CommanderName.add_command('trigger', callback, args)`` Adds commands to your Commander. Requires a ``trigger`` (the command the user will enter) and a ``callback`` (the function to be called by the trigger). Optionally you can set ``args`` to a number to accept that many arguments. Those arguments will be passed into your ``callback`` function in the order they are entered by the user.
* *get_input* - Usage: ``CommanderName.get_input(prompt)`` Prompts the user for input, similar to Python's built-in ``input()`` function. You can specify ``prompt`` on this function to override the default prompt of your Commander.

Arguments for commands can be ints, floats, strings, whatever. EasyPrompt treats them all as strings, becasue I'm not good at Python. ``trigger 1 2`` will call the function like so: ``function("1", "2")`` So if you need a specific data type, like an integer, I recommend you convert the arguments at the start of your function using ``int()`` or something similar.

When accepting multiple words as one argument, the user will have to put their string in quotations in order to use spaces, otherwise each word will be treated as its own argument. Example: ``Hello world!`` counts as two arguments whereas ``"Hello world!"`` counts as one.

### Simple Example Program
This program will prompt the user for two numbers, add them together, and print the result. It also an ``exit`` command for stopping the script cleanly.

	import EasyPrompt
	import sys

	def add_numbers(x, y):
		z = int(x) + int(y)
		print(f"{x} + {y} = {z}")
	
	def exit_program():
		print('Goodbye!')
		sys.exit(0)

	cmd = EasyPrompt.Commander()
	cmd.add_command('add', add_numbers, args=2)
	cmd.add_command('exit', exit_program)

	while True:
		cmd.get_input()

### Known Bugs
* Functions always seem to return ``None`` no matter what. I have no idea why this is happening. For now, if you want to have a specific command break a ``while`` loop, you'll have to use a try/except system, or something more clever.
