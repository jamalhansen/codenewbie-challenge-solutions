import pytest

import euchre.hand_sorter

def test_tim_is_dealt_a_hand_with_three_trump_cards():
    """
    Tim is dealt a hand with three trump cards.

    9h
    Ks
    Ac
    Qh
    Th
    """
    hand = "Hearts\n9h\nKs\nAc\nQh\nTh"

    # Tim sorts his hand with the sorter and sees
    # Hearts
    # Qh
    # Th
    # 9h
    # Ac
    # Ks
    expected = "Hearts\nQh\nTh\n9h\nAc\nKs"
    actual = euchre.hand_sorter.sort(hand)

    assert expected == actual

