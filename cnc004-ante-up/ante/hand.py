from ante.card import Card

def is_a_pair(cards):
    "Returns true if at least two cards are of the same value"
    values = [(Card(x)).card_value for x in cards]
    values.sort()

    has_pair = False
    last = ""

    while not has_pair and len(values) > 0:
        value = values.pop()
        has_pair = (last == value)
        last = value

    return has_pair

def is_three_of_a_kind(cards):
    "Returns true if at least three cards are of the same value"
    return True


class Hand:
    "This class represents a hand of 5 poker cards"
    def __init__(self):
        self.cards = []

    def add(self, card_value):
        "Adds a two character string representing a card to the hand"
        self.cards.append(card_value)

    def describe(self):
        "Describes the value of the hand"
        if is_a_pair(self.cards):
            return "Pair"
        else:
            return "Three of a Kind"

