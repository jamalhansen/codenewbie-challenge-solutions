"""This module contains the card information"""

def decode_suit(suit):
    """Decodes the long value of a suit name to the single character
    version
    """
    suits = {"Diamonds":"d", "Spades":"s", "Hearts":"h", "Clubs":"c"}
    return suits[suit]

def is_red(suit):
    """Returns true if the suit is red"""
    return suit in "dh"

class Card:
    """The card object encapsulates each card's suit and value data as
    well as the card sorting information"""

    def __init__(self, abbrev, trump):
        """Initializer accepts the two character abbreviation for the card
        as well as the enumarated trump suit value.

        Example:

        left_bower = Card("Js", "Clubs")
        """
        self.value = abbrev[0]
        self.suit = abbrev[1]
        self.trump_suit = decode_suit(trump)

    def sort_card_value(self):
        """Returns the sort value for the face value of the card"""
        sort = {'9':6, 'T':5, 'J':4, 'Q':3, 'K':2, 'A':1}

        return sort[self.value]

    def sort_trump_value(self):
        """Returns the sort value for the trump value of the card
        This places the trump suit cards ahead of the other cards
        """
        if self.is_trump():
            return 1
        else:
            return 2

    def sort_suit_value(self):
        """Returns the suit value of the card, this attemts to place the
        cards in red, black, red, black order
        """
        sort = {"c":1, "h":2, "s":3, "d":4}
        return sort[self.suit]

    def sort_bower_value(self):
        """This final sort value places the left and right Bowers ahead of
        other cards
        """
        if self.value != "J":
            return 3

        if is_red(self.suit) == is_red(self.trump_suit):
            if self.is_trump():
                return 1
            else:
                return 2
        else:
            return 3

    def sort_value(self):
        """This method returns a string containing the 4 sort values for the
        card concatenated by order of importance.  This is what is used to
        determine if any one card sorts before or after another
        """
        format_string = "{0}{1}{2}{3}"
        sort = format_string.format(self.sort_bower_value(),
                                    self.sort_trump_value(),
                                    self.sort_card_value(),
                                    self.sort_suit_value())
        return sort

    def output(self):
        """Recombines the value and suit for output to string"""
        return self.value + self.suit

    def is_trump(self):
        """Returns true if the card is of the trump suit"""
        return self.suit == self.trump_suit
