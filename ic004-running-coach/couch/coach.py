from couch.configuration import Configuration
from couch.workout_generator import WorkoutGenerator


class Coach:
    def __init__(self, ui):
        self._ui = ui
        self._config = Configuration(ui)

    def start(self, callback):
        self._config.get_name()

        text = "Welcome {0}, are you ready to start running? "
        question = text.format(self._config.username)
        ready = self._ui.ask(question)

        if ready.upper() == "YES":
            question = "Which week are you on {0}? ".format(
                    self._config.username)
            week = int(self._ui.ask(question))
            workout = int(self._ui.ask("Would you like variation 1, 2 or 3"))

            generator = WorkoutGenerator(week, workout)
            workout = generator.get_workout()
            self._ui.play(workout)
        callback()
