class Configuration:
    def __init__(self,ui):
        self._ui = ui
        self.username = ""

    def get_name(self):
        self.username = self._ui.ask("What is your name?")

