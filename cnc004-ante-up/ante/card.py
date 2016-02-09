class Card:
    def __init__(self, symbol):
        self.symbol = symbol

    @property
    def card_value(self):
        return self.symbol[0]

    @property
    def suit(self):
        return self.symbol[1]
