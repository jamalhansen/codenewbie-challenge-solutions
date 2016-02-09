import pytest

@pytest.fixture
def trumpless_clubs():
    return ("Hearts\n9c\nJc\nAc\nQc\nTc", "Hearts\nAc\nQc\nJc\nTc\n9c")

