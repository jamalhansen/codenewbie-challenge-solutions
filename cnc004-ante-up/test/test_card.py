import pytest


from ante.card import Card

def test_card_accepts_symbol():
    card = Card("AC")
    assert card.symbol == "AC"

def test_card_returns_card_value():
    card = Card("AC")
    assert card.card_value == "A"

def test_card_returns_card_suit():
    card = Card("KD")
    assert card.suit == "D"
