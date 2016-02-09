import pytest
import time
import random
import os


from couch.coach import Coach


def speak(message):
    os.system("espeak '{0}'".format(message))

def random_message():
    choices = ["You are doing great!",
                "Keep it up!",
                "You are almost there",
                "Do not stop believing!",
                "You have got this!",
                "You are moving so fast!",
                "You are leading the pack"]
    return random.choice(choices)

def split_times(total):
    length = int(total / 20)
    rem = total % 20

    split = [20] * length
    split[0] += rem
    return split

class CommandLineInterface():
    def __init__(self):
        self._coach = Coach(self)

    @property
    def coach(self):
        return self.coach

    def send(self, message):
        print(message)

    def receive(self):
        return input()

    def ask(self, message):
        return input(message)

    def run(self):
        self._coach.start(self.done)

    def done(self):
        pass

    def play(self, workout):
        while workout:
            message = "Great! Now lets, {0}".format(workout.output())
            self.send(message)
            times = split_times(workout.duration)

            for seconds in times:
                time.sleep(seconds)
                self.send(random_message())

            workout = workout.next_action

class CommandLineVoiceInterface():
    def __init__(self):
        self._coach = Coach(self)

    @property
    def coach(self):
        return self.coach

    def send(self, message):
        speak(message)

    def receive(self):
        return input()

    def ask(self, message):
        speak(message)

        return input(">")

    def run(self):
        self._coach.start(self.done)

    def done(self):
        pass

    def play(self, workout):
        while workout:
            message = "Great! Now lets, {0}".format(workout.output())
            self.send(message)
            times = split_times(workout.duration)

            for seconds in times:
                time.sleep(seconds)
                self.send(random_message())

            workout = workout.next_action
