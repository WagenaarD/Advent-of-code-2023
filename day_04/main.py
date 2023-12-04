"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 07:59:34
Part 1  - 08:04:15
Part 2  - 08:13:14
Cleanup - 
"""

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


# @print_function()
# def part_one(lines):
#     # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#     score = 0
#     for line in lines:
#         card_str, rest = line.split(': ')
#         winning, yours = rest.split(' | ')
#         winning = winning.split()
#         yours = yours.split()
#         correct = len([num for num in yours if num in winning])
#         if correct:
#             score += 2 ** (correct - 1)
#         print(correct, line)
#     return score

@print_function()
def part_two(lines: 'list[str]'):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    score = 0
    # stack = defaultdict(int)
    stack = lines.copy()
    while stack:
        line = stack.pop()
        score += 1
        card_str, rest = line.split(': ')
        card_idx = int(re.findall('\d+', card_str)[0])
        winning, yours = rest.split(' | ')
        winning = winning.split()
        yours = yours.split()
        correct = len([num for num in yours if num in winning])
        for idx in range(0, correct):
            stack.append(lines[card_idx + idx])

    return score



if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    # part_one(lines)
    part_two(lines)

