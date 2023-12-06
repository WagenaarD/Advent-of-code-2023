"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 
Part 1  - 
Part 2  - 
Cleanup - 
"""
# 08:06:21
# 08:12:40

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
    times = list(map(int, lines[0].split()[1:]))
    dists = list(map(int, lines[1].split()[1:]))
    print(times)
    print(dists)
    ans = 1
    for time, dist in zip(times, dists):
        solutions = 0
        for button_time in range(time):
            speed = button_time
            time_left = time - button_time
            new_dist = speed * time_left
            if new_dist > dist:
                solutions += 1
        ans *= solutions
        print(solutions)
    return ans



        


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)

