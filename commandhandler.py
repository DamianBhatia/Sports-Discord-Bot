class CommandHandler:

    # Constructor
    def __init__(self, client):
        self.client = client
        self.commands = []


    # Add a new command
    def add_command(self, command):
        if command not in self.commands:
            self.commands.append(command)
    

