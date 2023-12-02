"""
Advent of code challenge 2023
python3 main.py < in
python3 main.py < ex

Start   - 10:04:07
Part 1  - 10:17:42
Part 2  - 10:22:06
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

CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

lines = sys.stdin.read().strip().split('\n')

score_p1 = 0
score_p2 = 0
for idx, line in enumerate(lines):
    _, sets_str = line.split(':')
    set_lst = sets_str.split('; ')
    legal_p1 = True
    min_p2 = {'red': 0, 'green': 0, 'blue': 0}
    for cube_set in set_lst:
        for cubes in cube_set.split(', '):
            for color, max_items in CONFIG.items():
                if color not in cubes:
                    continue
                number_of_cubes = int(re.search('\d+', cubes).group())
                min_p2[color] = max(min_p2[color], number_of_cubes)
                if number_of_cubes > max_items:
                    legal_p1 = False
    if legal_p1:
        print('possible', idx)
        score_p1 += idx + 1
    score_p2 += math.prod(min_p2.values())

print('Part 1:', score_p1)
print('Part 2:', score_p2)
    
        
        

