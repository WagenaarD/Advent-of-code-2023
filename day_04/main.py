"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 07:59:34
Part 1  - 08:04:15
Part 2  - 08:13:14  13:40   07:08
Cleanup - 
"""

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from _utils.print_function import print_function
from collections import defaultdict
import re


def card_score(line: str) -> 'tuple(int, int)':
    """
    Returns the card idx (1 in example) and the score which are the number of numbers on the right
    side of the | also occurring on the lift side of the |. Example input:
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    card_str, rest = line.split(': ')
    card_idx = int(re.findall('\d+', card_str)[0])
    winning, yours = rest.split(' | ')
    winning = winning.split()
    yours = yours.split()
    correct = len([num for num in yours if num in winning])
    return (card_idx, correct)


@print_function()
def part_one(lines: 'list[str]') -> int:
    score = 0
    for line in lines:
        _, correct = card_score(line)
        if correct:
            score += 2 ** (correct - 1)
    return score


@print_function()
def part_two(lines: 'list[str]') -> int:
    score = 0
    stack = defaultdict(int)
    for line in lines:
        stack[line] = 1
    while stack:
        line = list(stack)[0]
        count = stack.pop(line)
        score += count
        card_idx, correct = card_score(line)
        for idx in range(0, correct):
            stack[lines[card_idx + idx]] += count
    return score


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

