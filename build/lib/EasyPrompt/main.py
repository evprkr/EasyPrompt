# EasyPrompt v1.0.0
# by Evan Parker (@evprkr)
# https://github.com/evprkr/EasyPrompt

import inspect, shlex

# Main Commander Class
class Commander:
    def __init__(self, prompt=None, commands=None, previous_cmd=None):
        if prompt == None: self.prompt = 'COMMAND: '
        else: self.prompt = prompt

        self.commands = []
        self.previous_cmd = previous_cmd

    def get_input(self, prompt=None, new_line=True):
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
                    print(f'Error: expected {arg_num} arguments, got {len(input_split)-1}\n')
                    return

                if len(input_split) > 1:
                    cmd_args = []
                    for i in range(1, arg_num+1):
                        cmd_args.append(input_split[i])

                    callback(*cmd_args)
                    print('')
                    return

                callback()
                print('')
                return
        else:
            print(f"Command not found: '{input_split[0]}'\n")

    def add_command(self, trigger, callback, args=None):
       command = [trigger, callback, args]
       self.commands.append(command)
