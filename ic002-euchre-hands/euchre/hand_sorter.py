""" The Hand sorter module sorts "hand" of Euchre "cards" that are passed
into it in the following format:

Trump Suit (Diamonds, Clubs, Hearts, Spades)
Card 1
Card 2
Card 3
Card 4
Card 5

Where the cards are 2 character pairs representing the value and the suit:

<value><suit>

Values (9 = Nine
        T = Ten
        J = Jack
        Q = Queen
        K = King
        A = Ace)

Suits  (d = Diamonds
        s = Spades
        c = Clubs
        h = Hearts)

Examples:
    9h = Nine of Hearts
    As = Ace of Spades
"""
from euchre.card import Card


def sort(hand):
    """Called to sort a hand by Euchre rules """
    lines = split_hand(hand)
    cards = build_hand(lines)
    cards.sort(key=lambda x: x.sort_value(), reverse=False)
    output_string = "\n".join(list(map(lambda x: x.output(), cards)))

    return "{0}\n{1}".format(lines[0], output_string)

def split_hand(hand):
    """Parses the input format into individual lines / values"""
    if hand == None:
        raise ValueError("Invalid hand: None")

    lines = hand.split("\n")
    if len(lines) != 6:
        raise ValueError("Invalid hand: {0}".format(hand))

    return lines

def build_hand(hand):
    """Converts the individual card values to a List of Cards"""
    encoded = hand[1:6]
    output = list()

    for code in encoded:
        output.append(Card(code, hand[0]))

    return output
