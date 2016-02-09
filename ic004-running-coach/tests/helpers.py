import pytest


from couch.coach import Coach

class TestUi():
    def __init__(self):
        self.queue = []
        self._coach = Coach(self)

    @property
    def coach(self):
        return self.coach

    def displays(self, text):
        self.queue.insert(0,("displays", text))

    def enters(self, text):
        self.queue.insert(0,("enters", text))

    def send(self, actual):
        assert len(self.queue) > 0
        action, expected = self.queue.pop()
        assert action == "displays", expected
        assert actual == expected

    def receive(self):
        assert len(self.queue) > 0
        action, text = self.queue.pop()
        assert action == "enters"
        return text

    def ask(self, actual):
        self.send(actual)
        return self.receive()

    def run(self):
        self._coach.start(self.done)

    def done(self):
        assert len(self.queue) == 0

    def play(self, workout):
        pass


@pytest.fixture
def ui():
    return TestUi()

