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
from functools import cmp_to_key


class Hand:
    def __init__(self, hand):
        self.hand: str = hand
    
    def get_val(self, joker = False) -> int:
        if joker:
            cards = CARDS_NOJ
            no_jokers = self.hand.count('J')
        else:
            cards = CARDS
            no_jokers = 0
        same_of_one = max([self.hand.count(c) for c in cards])
        if same_of_one + no_jokers == 5:
            return 7
        elif same_of_one + no_jokers == 4:
            return 6
        elif no_jokers == 0 and (any([self.hand.count(c) == 3 for c in cards]) and any([self.hand.count(c) == 2 for c in cards])):
            return 5
        elif no_jokers == 1 and (sum([self.hand.count(c) == 2 for c in cards]) == 2):
            return 5
            # FH: Two jokers and one pair? -> is always 4OAK!
        elif same_of_one + no_jokers == 3:
            return 4
        elif sum([self.hand.count(c) == 2 for c in cards]) == 2:
            return 3
            # TP: One joker and one pair? -> Is always 3OAK
        elif same_of_one + no_jokers == 2:
            return 2
        else:
            return 1

    def comp(self, other: 'Hand', joker = False) -> int:
        """returns 1 if self > higher, -1 if self < higher and 0 if self == higher"""
        cards = CARDS_NOJ + ['J'] if joker else CARDS
        value_diff = self.get_val(joker) - other.get_val(joker)
        if value_diff > 0:
            # self has higher value
            return 1
        elif value_diff < 0:
            return -1
        for card_self, card_other in zip(self.hand, other.hand):
            if cards.index(card_other) > cards.index(card_self):
                # self has higher value
                return 1
            elif cards.index(card_other) < cards.index(card_self):
                return -1
        return 0


@print_function()
def part_one(lines):
    hand_list = [(Hand(hand), int(bid)) for hand, bid in [line.split() for line in lines]]
    hand_list.sort(key = cmp_to_key(lambda h1, h2: h1[0].comp(h2[0])))
    return sum([idx * bid for idx, (hand, bid) in enumerate(hand_list, 1)])


@print_function()
def part_two(lines):
    hand_list = [(Hand(hand), int(bid)) for hand, bid in [line.split() for line in lines]]
    hand_list.sort(key = cmp_to_key(lambda h1, h2: h1[0].comp(h2[0], True)))
    return sum([idx * bid for idx, (hand, bid) in enumerate(hand_list, 1)])


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

