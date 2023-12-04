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
def main(lines: 'list[str]') -> int:
    score_p1, score_p2 = 0, [1] * len(lines)
    for idx, line in enumerate(lines):
        left, right = line.split(': ')[1].split('|')
        correct = len(set(left.split()) & set(right.split()))
        if correct:
            score_p1 += 2 ** (correct - 1)
        for idx2 in range(idx+1, idx+correct+1):
            score_p2[idx2] += score_p2[idx]
    return score_p1, sum(score_p2)


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    main(lines)

