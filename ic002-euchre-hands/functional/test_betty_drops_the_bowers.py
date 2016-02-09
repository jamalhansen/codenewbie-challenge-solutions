import pytest

import euchre.hand_sorter

def test_betty_drops_the_bowers():
    """
    Betty has never played euchre before and is humoring her friends by
    playing at all.  On her first hand she is dealt the following hand.

    9s
    Js
    Jc
    Jh
    Kh
    """
    hand = "Clubs\n9s\nJs\nJc\nJh\nKh"

    # Betty sorts his hand with the sorter and sees
    # Clubs
    # Jc
    # Js
    # Kh
    # Jh
    # 9s
    expected = "Clubs\nJc\nJs\nKh\nJh\n9s"
    actual = euchre.hand_sorter.sort(hand)

    assert expected == actual

    # Seeing that the queen of hearts is missing, Billy feels a pang of loss
    # He leaves the game to call his high-school friend Nancy.
