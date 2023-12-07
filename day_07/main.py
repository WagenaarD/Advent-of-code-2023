"""
Advent of code challenge 2023
python3 ../_utils/get_aoc_in.py
python3 main.py < in
"""
# Start, Part 1, Part 2
# 11:05:45
# 11:35:43
# 11:51:39

CARDS = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
JCARDS = 'A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J'.split(', ')
CARDS_NOJ = JCARDS[:-1]

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from _utils.print_function import print_function
import itertools as it
from dataclasses import dataclass, field
from collections import defaultdict
import re
import numpy as np
from pprint import pprint
from functools import cache
import math
from functools import cmp_to_key

def comp_card(card_1, card_2):
    return CARDS.index(card_2) - CARDS.index(card_1)

class Hand:
    def __init__(self, hand):
        self.hand: str = hand

    @property
    def value_j(self):
        if max([self.hand.count(card) for card in CARDS_NOJ]) + self.hand.count('J') == 5:
            #7 Five of a kind, where all five cards have the same label: AAAAA
            return 7
        elif max([self.hand.count(card) for card in CARDS_NOJ]) + self.hand.count('J') == 4:
            #6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
            return 6
        elif self.hand.count('J') == 0 and (any([self.hand.count(card) == 3 for card in CARDS_NOJ]) and any([self.hand.count(card) == 2 for card in CARDS_NOJ])):
            # FH: No joker
            #5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            return 5
        elif self.hand.count('J') == 1 and (sum([self.hand.count(card) == 2 for card in CARDS_NOJ]) == 2):
            # FH: One joker AND two pair
            #5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            return 5
            # FH: Two jokers and one pair? -> is always 4OAK!
        elif max([self.hand.count(card) for card in CARDS_NOJ]) + self.hand.count('J') == 3:
            #4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
            return 4
        elif sum([self.hand.count(card) == 2 for card in CARDS]) == 2:
            #3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            return 3
            # TP: One joker and one pair? -> Is always 3OAK
        elif max([self.hand.count(card) for card in CARDS_NOJ]) + self.hand.count('J') == 2:
            #2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
            return 2
        else:
            #1 High card, where all cards' labels are distinct: 23456
            return 1
    
    @property
    def value(self):
        if max([self.hand.count(card) for card in CARDS]) == 5:
            #7 Five of a kind, where all five cards have the same label: AAAAA
            return 7
        elif max([self.hand.count(card) for card in CARDS]) == 4:
            #6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
            return 6
        elif any([self.hand.count(card) == 3 for card in CARDS]) and any([self.hand.count(card) == 2 for card in CARDS]):
            #5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            return 5
        elif max([self.hand.count(card) for card in CARDS]) == 3:
            #4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
            return 4
        elif sum([self.hand.count(card) == 2 for card in CARDS]) == 2:
            #3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            return 3
        elif max([self.hand.count(card) for card in CARDS]) == 2:
            #2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
            return 2
        else:
            #1 High card, where all cards' labels are distinct: 23456
            return 1
    
    def __str__(self) -> str:
        return f'({self.hand})'

    def __repr__(self) -> str:
        return str(self)


    def comp(self, other: 'Hand') -> int:
        if self.value > other.value:
            # self has higher value
            return 1
        elif self.value < other.value:
            # self has lower value
            return -1
        else:
            for card_self, card_other in zip(self.hand, other.hand):
                if CARDS.index(card_other) < CARDS.index(card_self):
                    # self has lower value
                    return -1
                elif CARDS.index(card_other) > CARDS.index(card_self):
                    # self has higher value
                    return 1
        return 0

    def comp_j(self, other: 'Hand') -> int:
        if self.value_j > other.value_j:
            # self has higher value
            return 1
        elif self.value_j < other.value_j:
            # self has lower value
            return -1
        else:
            for card_self, card_other in zip(self.hand, other.hand):
                if JCARDS.index(card_other) < JCARDS.index(card_self):
                    # self has lower value
                    return -1
                elif JCARDS.index(card_other) > JCARDS.index(card_self):
                    # self has higher value
                    return 1

        

def compare_hands(hand_1, hand_2):
    return 





@print_function()
def part_one(lines):
    # print(CARDS)
    pairs = [line.split() for line in lines]
    hand_list = [(Hand(hand), int(bid)) for hand, bid in pairs]
    # hands = [hand for hand, bid in pairs]
    # print(hand_list)
    # bids = [int(bid) for hand, bid in pairs]
    hand_list.sort(key = cmp_to_key(lambda h1, h2: h1[0].comp(h2[0])))
    # print('')
    # pprint([(hand, hand.value, bid) for hand, bid in hand_list])
    ans = 0
    for idx, (hand, bid) in enumerate(hand_list, 1):
        ans += idx * bid
    return ans


@print_function()
def part_two(lines):
    # print(CARDS)
    pairs = [line.split() for line in lines]
    hand_list = [(Hand(hand), int(bid)) for hand, bid in pairs]
    # hands = [hand for hand, bid in pairs]
    # print(hand_list)
    # bids = [int(bid) for hand, bid in pairs]
    hand_list.sort(key = cmp_to_key(lambda h1, h2: h1[0].comp_j(h2[0])))
    # print('')
    # pprint([(hand, hand.value, bid) for hand, bid in hand_list])
    ans = 0
    for idx, (hand, bid) in enumerate(hand_list, 1):
        ans += idx * bid
    return ans
        

    


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    print(part_one(lines) == 250120186)
    part_two(lines)

