"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 09:26:18
Part 1  - 09:38:09  11:51   07:09 (my time vs. leaderboard)
Part 2  - 09:47:59  21:41   11:37
Cleanup - 10:49:56
"""

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from _utils.print_function import print_function
import re
import math
            
@print_function()
def main(input: 'list[str]'):
    digits = []
    gears = []
    symbols = []
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '*':
                gears.append((r, c))
            if char not in '1234567890.':
                symbols.append((r, c))
            # if not the start of a number, ignore this cell
            if not char.isdigit():
                continue
            if c > 0 and line[c-1].isdigit():
                continue
            # get total number
            value_str = re.search('\d+', input[r][c:]).group()
            value = int(value_str)
            # add digit
            digits.append((value, [(r + rr, c + cc) for rr in (-1,0,1) for cc in range(-1, 1+len(value_str))]))
    # Scoring
    score_p1 = 0
    for dig in digits:
        adjacent = [sym for sym in symbols if sym in dig[1]]
        if adjacent:
            score_p1 += dig[0]
    score_p2 = 0
    for gear in gears:
        adjacent_digits = [dig[0] for dig in digits if gear in dig[1]]
        if len(adjacent_digits) == 2:
            score_p2 += math.prod(adjacent_digits)

    return (score_p1, score_p2)

if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')

    main(lines)
