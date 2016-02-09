import pytest

import euchre.hand_sorter

def test_nancy_is_dealt_a_hand_of_nines():
    """
    Nancy, sitting on the shores of Lake Michigan is playing a game of
    Euchre with her grandmother.  She is dealt a hand containing four nines.

    9h
    9c
    9d
    Kh
    9s
    """
    hand = "Clubs\n9h\n9c\n9d\nKh\n9s"

    # Nancy sorts her hand with the sorter and sees
    # Clubs
    # 9c
    # Kh
    # 9h
    # 9s
    # 9d
    expected = "Clubs\n9c\nKh\n9h\n9s\n9d"
    actual = euchre.hand_sorter.sort(hand)

    assert expected == actual

    # Nancy is 9 and decides that this is her lucky hand
