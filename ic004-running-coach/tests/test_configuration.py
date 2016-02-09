import pytest


from tests.helpers import ui
from couch.configuration import Configuration


def test_configuration_get_info_gets_info(ui):
    config = Configuration(ui)

    ui.displays("What is your name?")
    ui.enters("Test")

    config.get_name()
    assert config.username == "Test"
