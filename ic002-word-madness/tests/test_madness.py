import pytest
from madness.madness import *
from madness.prompt import Prompt

@pytest.fixture
def madness():
    return Madness()

@pytest.fixture
def story():
    return "import { pronoun }!"

def test_madness_has_story_attribute(madness):
    assert hasattr(madness, "story")

def test_get_prompts_returns_a_list(madness, story):
    madness.story = story
    prompts = madness.get_prompts()
    assert isinstance(prompts, list)

def test_get_prompts_returns_a_value(madness, story):
    madness.story = story
    prompts = madness.get_prompts()
    assert 1 == len(prompts)

def test_get_prompts_returns_a_prompt(madness, story):
    madness.story = story
    prompts = madness.get_prompts()

    for prompt in prompts:
        assert isinstance(prompt, Prompt)

def test_madness_can_split_prompt(madness, story):
    madness.story = story
    prompts, _ = madness.split_story()
    assert 1 == len(prompts)
    assert "{ pronoun }" == prompts[0]

def test_madness_can_split_story(madness, story):
    madness.story = story
    _, story = madness.split_story()
    assert 2 == len(story)
    assert "import " == story[0]
    assert "!" == story[1]

def test_get_prompts_returns_prompt_from_story(madness, story):
    madness.story = story
    prompts = madness.get_prompts()
    assert prompts[0].text == "pronoun"

def test_clean_prompt_removes_curly_braces():
    assert "foo" == clean_prompt("{foo}")

def test_clean_prompt_strips_spaces():
    assert "foo bar" == clean_prompt("{ foo bar }")

def test_ensue_hilarity_outputs_story(madness, story):
    madness.story = story
    prompts = madness.get_prompts()
    prompts[0].value = "this"
    assert "import this!" == madness.ensue_hilarity()

