import pytest

import euchre.hand_sorter

def test_billy_is_dealt_a_hand_without_trump_effects_and_of_same_suit():
    """
    Billy through a stroke of fate or misfortune is dealt a hand comprised
    entirely of hearts.  Spades are trump so there are no effects from
    trump.  His cards as he recieves them are :

    Kh
    Jh
    Ah
    9h
    Th
    """
    hand = "Spades\nKh\nJh\nAh\n9h\nTh"

    # Billy sorts his hand with the sorter and sees
    # Spades
    # Ah
    # Kh
    # Jh
    # Th
    # 9h
    expected = "Spades\nAh\nKh\nJh\nTh\n9h"
    actual = euchre.hand_sorter.sort(hand)

    assert expected == actual

    # Seeing that the queen of hearts is missing, Billy feels a pang of loss
    # He leaves the game to call his high-school friend Nancy.
