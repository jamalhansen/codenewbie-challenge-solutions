#!/usr/bin/python3.4

import sys

import euchre.hand_sorter

deal = sys.stdin.read()
deal = deal.strip()
hand = euchre.hand_sorter.sort(deal)
print("----Unsorted----")
print(deal)
print("\n----Sorted----")
print(hand)
