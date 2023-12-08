"""
Advent of code challenge 2023
python3 ../_utils/get_aoc_in.py
python3 main.py < in
"""
# Start, Part 1, Part 2
# 09:23:08
# 09:31:06

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


@print_function()
def part_one(lines):
    dirs = lines[0]
    elements = {}
    for line in lines[2:]:
        key, left, right = re.findall('\w+', line)
        elements[key] = {'L': left, 'R': right}
    pprint(dirs)
    pprint(elements)
    pos = 'AAA'
    idx = 0
    while pos != 'ZZZ':
        dir = dirs[idx % len(dirs)]
        print(dir, pos, idx, elements[pos], elements[pos][dir])
        pos = elements[pos][dir]
        idx += 1
    return idx

if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)

