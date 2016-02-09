import pytest

import euchre.hand_sorter
from euchre.card import Card
from helpers import *


def test_hand_sorter_can_sort(trumpless_clubs):
    hand, expected = trumpless_clubs
    actual = euchre.hand_sorter.sort(hand)
    assert expected == actual

def test_throws_value_error_on_empty_string():
    try:
        euchre.hand_sorter.sort("")
        assert False
    except ValueError:
        assert True

def test_throws_value_error_on_string_that_is_less_than_six_lines():
    invalids = ["1", "1\n2", "1\n2\n3", "1\n2\n3\n4", "1\n2\n3\n4\n5"]

    for invalid in invalids:
        try:
            euchre.hand_sorter.sort(invalid)
            assert False
        except ValueError:
            assert True

def test_value_error_shows_invalid_hand():
    try:
        euchre.hand_sorter.sort("wubbly")
        assert False
    except ValueError as e:
        assert "wubbly" in e.args[0]

def test_value_error_thown_on_null_hand():
    try:
        euchre.hand_sorter.sort(None)
        assert False
    except ValueError as e:
        assert "None" in e.args[0]

def test_split_hand_returns_six_lines(trumpless_clubs):
    lines = euchre.hand_sorter.split_hand(trumpless_clubs[0])
    assert 6 == len(lines)

def test_will_build_hand():
    hand = ['Diamonds', '9h', 'Kc', 'As', 'Jd', '9s']
    object_list = euchre.hand_sorter.build_hand(hand)
    assert len(object_list) == 5

    for card in object_list:
        assert type(card) is Card
