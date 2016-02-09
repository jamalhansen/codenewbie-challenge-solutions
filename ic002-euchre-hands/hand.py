#!/usr/bin/python3.4

from random import randrange, shuffle

# build a Euchre deck
cards = []
faces = ['9', 'T', 'J', 'Q', 'K', 'A']
suits = ['d', 'c', 's', 'h']


for face in faces:
    for suit in suits:
        card = face + suit
        cards.append(card)

# choose trump
suit_names = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
print(suit_names[randrange(0, 4)])

# deal a hand
shuffle(cards)
for dealt in cards[0:5]:
    print(dealt)
