class Activity:
    def __init__(self, name, duration, next_action=None):
        self._name = name
        self._duration = duration
        self._next_action = next_action

    @property
    def name(self):
        return self._name

    @property
    def duration(self):
        return self._duration

    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, next_action):
        self._next_action = next_action

    def output(self):
        return "{0} for {1} seconds".format(self._name, self._duration)

    def add_to_tail(self, activity):
        if self._next_action:
            self._next_action.add_to_tail(activity)
        else:
           self._next_action = activity

    def chain_length(self):
        if self._next_action:
            return (self._next_action.chain_length() + 1)
        else:
            return 1

class Jog(Activity):
    def __init__(self, duration, next_action=None):
        super().__init__("jog", duration, next_action)

class Walk(Activity):
    def __init__(self, duration, next_action=None):
        super().__init__("walk", duration, next_action)

