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


def read_card(line: str) -> 'tuple(int, int)':
    card_str, rest = line.split(': ')
    left, right = rest.split(' | ')
    return (int(card_str[5:]), len(set(left.split()) & set(right.split())))

@print_function()
def part_one(lines: 'list[str]') -> int:
    score = 0
    for line in lines:
        _, correct = read_card(line)
        if correct:
            score += 2 ** (correct - 1)
    return score


@print_function()
def part_two(lines: 'list[str]') -> int:
    score = 0
    stack = defaultdict(int, {line: 1 for line in lines})
    while stack:
        line = list(stack)[0]
        count = stack.pop(line)
        score += count
        card_idx, correct = read_card(line)
        for idx in range(0, correct):
            stack[lines[card_idx + idx]] += count
    return score


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

