import pytest


from ante.hand import *


def test_add_card_to_hand():
    hand = Hand()
    hand.add("AS")
    assert hand.cards[0] == "AS"

def test_describe_returns_a_description_of_the_hand():
    hand = Hand()
    hand.add("AS")
    hand.add("AD")
    hand.add("AC")
    hand.add("3H")
    hand.add("9D")

    assert hand.describe() == "Three of a Kind"

@pytest.fixture
def pair():
    return ["3S", "3D", "4H", "6S", "KC"]

@pytest.fixture
def high_card():
    return ["3S", "6D", "9H", "QC", "KS"]

def test_can_identify_a_pair(pair):
    assert is_a_pair(pair)

def test_does_not_identify_high_card_as_pair(high_card):
    assert not is_a_pair(high_card)

def test_can_identify_three_of_a_kind(three_of_a_kind):
    assert is_three_of_a_kind(three_of_a_kind)

def test_does_not_identify_pair_as_three_of_a_kind(pair):
    assert not is_three_of_a_kind(pair)

def test_does_not_identify_high_card_as_three_of_a_kind(high_card):
    assert not is_three_of_a_kind(high_card)

