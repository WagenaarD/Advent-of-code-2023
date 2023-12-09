"""
Advent of code challenge 2023
python3 ../_utils/get_aoc_in.py
python3 main.py < in
"""
# Start, Part 1, Part 2
# 08:14:39
# 08:46:41 -teken vergeten bij regex, anders klaar na 8 min.
# 11:23:22 met pauze

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from aoc_tools import print_function


@print_function()
def main(lines):
    score_p1 = 0
    score_p2 = 0
    for line in lines:
        deriv_lines = [list(map(int, line.split()))]
        while not all(num == 0 for num in deriv_lines[-1]):
            deriv_lines.append([second-first for first, second in zip(deriv_lines[-1], deriv_lines[-1][1:])])
        extra_last = 0
        extra_first = 0
        for deriv in deriv_lines[::-1]:
            extra_last += deriv[-1]
            extra_first = deriv[0] - extra_first
        score_p1 += extra_last
        score_p2 += extra_first
    return (score_p1, score_p2)


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    print(main(lines) == (1702218515, 925))

