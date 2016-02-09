import pytest


from madness.prompt import Prompt

@pytest.fixture
def noun():
    return Prompt("noun")

def test_prompt_has_text(noun):
    assert hasattr(noun, "text")

def test_can_set_text(noun):
    assert noun.text == "noun"

def test_prompt_has_value(noun):
    assert hasattr(noun, "value")
