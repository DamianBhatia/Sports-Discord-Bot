class CommandHandler:

    # Constructor
    def __init__(self, client):
        self.client = client
        self.commands = []


    # Add a new command
    def add_command(self, command):
        if command not in self.commands:
            self.commands.append(command)


    # Find the command and run the corresponding function
    def execute(self, message, args):
        for command in self.commands:
            if command.trigger == args[0]:
                command.func()
                

class Command:

    # Constructor
    def __init__(self, trigger, num_args, desc, func):
        self.trigger = trigger
        self.num_args = num_args
        self.desc = desc
        self.func = func