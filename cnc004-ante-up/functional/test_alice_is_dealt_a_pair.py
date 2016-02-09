import pytest


from ante.hand import Hand


def test_alice_is_dealt_a_pair_of_aces():
    # Alice is new to poker and sits down to a game.
    # She is dealt five cards. She
    # Looks down and finds the following
    #    Ace of Spades
    #    Ace of Hearts
    #    Five of Clubs
    #    Jack of Diamonds
    #    Seven of Hearts
    hand = Hand()
    hand.add("AS")
    hand.add("AH")
    hand.add("5C")
    hand.add("JD")
    hand.add("7H")

    # She evaluates the cards in her hand
    value = hand.describe()

    # Alice find that her hand contains A Pair
    assert value == "Pair"
