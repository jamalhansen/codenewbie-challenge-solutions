from couch.user_interfaces import CommandLineInterface
from couch.user_interfaces import CommandLineVoiceInterface

result = input("Do you have espeak installed?")

if result[0].upper() == "Y":
    ui = CommandLineVoiceInterface()
else:
    ui = CommandLineInterface()

ui.run()
