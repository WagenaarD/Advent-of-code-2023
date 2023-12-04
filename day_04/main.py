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


@print_function()
def part_one(lines: 'list[str]') -> int:
    score = 0
    for line in lines:
        left, right = line.split(': ')[1].split('|')
        correct = len(set(left.split()) & set(right.split()))
        if correct:
            score += 2 ** (correct - 1)
    return score


@print_function()
def part_two(lines: 'list[str]') -> int:
    score = [1] * len(lines)
    for idx, line in enumerate(lines):
        left, right = line.split(': ')[1].split('|')
        correct = len(set(left.split()) & set(right.split()))
        for idx2 in range(idx+1, idx+correct+1):
            score[idx2] += score[idx]
    return sum(score)


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

