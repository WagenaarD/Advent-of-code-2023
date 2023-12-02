"""
Advent of code challenge 2023
python3 main.py < in
python3 main.py < ex

Start   - 10:04:07
Part 1  - 10:17:42
Part 2  - 
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

CONFIG = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

lines = sys.stdin.read().strip().split('\n')

score = 0
for idx, line in enumerate(lines):
    _, sets_str = line.split(':')
    set_lst = sets_str.split('; ')
    legal = True
    for cube_set in set_lst:
        # print(cube_set)
        for cubes in cube_set.split(', '):
            # print(cubes)
            for color, max_items in CONFIG.items():
                if color not in cubes:
                    continue
                number_of_cubes = int(re.search('\d+', cubes).group())
                # print(color, max_items, cubes, number_of_cubes, number_of_cubes > max_items)
                if number_of_cubes > max_items:
                    legal = False
    if legal:
        print('possible', idx)
        score += idx + 1

print('Part 1:', score)
    
        
        

