"""
Advent of code challenge 2023
python3 main.py < in
python3 main.py < ex

Start   - 10:04:07
Part 1  - 10:17:42 (leaderboard 04:10)
Part 2  - 10:22:06 (leaderboard filled in 06:15)
"""

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from _utils.print_function import print_function
import math

BAG_CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

@print_function()
def main(lines):
    score_p1 = 0
    score_p2 = 0
    for idx, line in enumerate(lines):
        _, sets_str = line.split(': ')
        legal_p1 = True
        min_p2 = {key: 0 for key in BAG_CONFIG}
        for cube_str in sets_str.replace(';', ',').split(', '):
            no_cubes_str, color = cube_str.split()
            min_p2[color] = max(min_p2[color], int(no_cubes_str))
            if int(no_cubes_str) > BAG_CONFIG[color]:
                legal_p1 = False
        if legal_p1:
            score_p1 += idx + 1
        score_p2 += math.prod(min_p2.values())
    return(score_p1, score_p2)
    
if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    main(lines)
    
        

