import pytest

from euchre.card import Card, decode_suit, is_red
from helpers import *

def test_card_has_value():
    card = Card("9h", "Clubs")
    assert card.value == '9'

def test_nine_card_has_sort_value_of_six():
    card = Card("9h", "Diamonds")
    assert card.sort_card_value() == 6

def test_ten_card_has_sort_value_of_five():
    card = Card("Th", "Diamonds")
    assert card.sort_card_value() == 5

def test_jack_card_has_sort_value_of_four():
    card = Card("Jh", "Diamonds")
    assert card.sort_card_value() == 4

def test_queen_card_has_sort_value_of_three():
    card = Card("Qh", "Diamonds")
    assert card.sort_card_value() == 3

def test_king_card_has_sort_value_of_two():
    card = Card("Kh", "Diamonds")
    assert card.sort_card_value() == 2

def test_ace_card_has_sort_value_of_one():
    card = Card("Ah", "Diamonds")
    assert card.sort_card_value() == 1

def test_card_outputs_encoded_value():
    card = Card("Ah", "Diamonds")
    assert card.output() == "Ah"

def test_card_accepts_trump_suit_upon_creation():
    card = Card("Ah", "Diamonds")
    assert card.trump_suit == "d"

def test_decode_suit_decodes_all_suits():
    card = Card("Ah", "Diamonds")
    assert decode_suit("Diamonds") == "d"
    assert decode_suit("Clubs") == "c"
    assert decode_suit("Hearts") == "h"
    assert decode_suit("Spades") == "s"

def test_trump_card_outputs_sort_of_one():
    card = Card("Ad", "Diamonds")
    assert card.sort_trump_value() == 1

def test_non_trump_card_outputs_sort_of_two():
    card = Card("Ad", "Spades")
    assert card.sort_trump_value() == 2

def test_suit_sorts_clubs_first():
    card = Card("9c", "Hearts")
    assert card.sort_suit_value() == 1

def test_suit_sorts_hearts_second():
    card = Card("9h", "Clubs")
    assert card.sort_suit_value() == 2

def test_suit_sorts_spades_third():
    card = Card("9s", "Hearts")
    assert card.sort_suit_value() == 3

def test_suit_sorts_diamonds_fourth():
    card = Card("9d", "Clubs")
    assert card.sort_suit_value() == 4

def test_sort_combines_sorts():
    card = Card("9s", "Diamonds")
    assert card.sort_value() == "263"

def test_sort_jack_bauer_errr_right_jack_bower():
    card = Card("Js", "Spades")
    assert card.sort_bower_value() == 1

def test_sort_left_jack_bower():
    card = Card("Jc", "Spades")
    assert card.sort_bower_value() == 2

def test_not_jack_bower():
    card = Card("Jh", "Spades")
    assert card.sort_bower_value() == 3

def test_sort_combines_sorts():
    card = Card("9s", "Diamonds")
    assert card.sort_value() == "3263"

def test_can_tell_suit_color():
    assert is_red("d")
    assert is_red("h")
    assert not is_red("c")
    assert not is_red("s")
