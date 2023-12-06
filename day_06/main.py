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
# 08:27:11

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
    times = map(int, lines[0].split()[1:])
    dists = map(int, lines[1].split()[1:])
    ans = 1
    for time, dist in zip(times, dists):
        solutions = 0
        for button_time in range(time):
            # speed = button_time
            # time_left = time - button_time
            # new_dist = speed * time_left
            # if new_dist > dist: solutions += 1
            solutions += button_time * (time - button_time) > dist
        ans *= solutions
    return ans

@print_function()
def part_two(lines):
    record_time = int(''.join(lines[0].split()[1:]))
    record_dist = int(''.join(lines[1].split()[1:]))
    # new_dist = speed * time_left
    #          = button_time * (record_time - button_time)
    #          = - button_time**2 + record_time * button_time
    # trying to find point where new_dist == record_dist
    # record_dist = - button_time**2 + record_time * button_time
    # button_time**2 - record_time * button_time + record_dist = 0
    # ABC formula with
    #  X = button_time
    #  a = 1, b = -record_time, c = record_dist
    #  X = (-b +/- sqrt(b**2 - 4ac)) / 2a
    #  button_time = (record_time +/- sqrt(record_time**2 - 4*record_dist)) / 2
    range_start = (record_time - math.sqrt(record_time**2 - 4*record_dist)) / 2
    range_end = (record_time + math.sqrt(record_time**2 - 4*record_dist)) / 2
    ans = math.floor(range_end) - math.ceil(range_start)
    return ans

@print_function()
def part_two_brute_1(lines):
    time = int(''.join(lines[0].split()[1:]))
    dist = int(''.join(lines[1].split()[1:]))
    ans = 0
    for button_time in range(time):
        ans += button_time * (time - button_time) > dist
    return ans


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)
    part_two_brute_1(lines)
    # part_one(...) = 140220 (2.5e-05 s)
    # part_two(...) = 39570184 (5e-06 s)
    # part_two_brute_1(...) = 39570185 (3.11231 s)

