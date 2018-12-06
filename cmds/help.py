import commands

def help(*args):
   msg = "Напиши:\n"
   for cmd in commands.cmds:
        msg += "&#9726; '" + cmd.keys[0] + "' - " + cmd.description + '\n'
   return msg

help_command = commands.Command()

help_command.keys = ["помощь", "помоги", "что", "help", "?"]
help_command.description = "открою справку"
help_command.process = help