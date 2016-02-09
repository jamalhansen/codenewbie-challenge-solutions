import pytest
from madness.madness import Madness

def test_alice_tries_word_madness():
    # Alice tries word madness for the first time and makes a silly story
    story = "Mary had a little { animal }."

    # Alice loads up a story
    madness = Madness()
    madness.story = story

    # Madness prompts her for a word to fill in
    prompts = madness.get_prompts()
    assert 1 == len(prompts)
    assert prompts[0].text == "animal"

    # Alice returns the word
    prompts[0].value = "goat"

    # The completed story is output for her.
    expected = "Mary had a little goat."
    assert expected == madness.ensue_hilarity()
