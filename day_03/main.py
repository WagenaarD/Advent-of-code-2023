"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 09:26:18
Part 1  - 09:38:09
Part 2  - 09:47:59
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


@print_function()
def part_one(input: 'list[str]'):
    score = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            # if not the start of a number, ignore this cell
            if not input[y][x].isdigit():
                continue
            if x > 0:
                if input[y][x-1].isdigit():
                    continue
            # get total number
            value_str = re.search('\d+', input[y][x:]).group()
            value = int(value_str)
            # check if adjacent to any symbol
            adjacent_symbol = False
            for yy in range(max(0, y-1), min(len(input), y+2)):
                for xx in range(max(0, x-1), min(len(input[y]), x+len(value_str)+1)):
                    if input[yy][xx].isdigit() or input[yy][xx] == '.':
                        pass
                    else:
                        adjacent_symbol = True
            if adjacent_symbol:
                score += value
                print(value)
    return score
            
@print_function()
def part_two(input: 'list[str]'):
    score = 0
    digits = set()
    gears = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '*':
                gears.add((x, y))
            # if not the start of a number, ignore this cell
            if not input[y][x].isdigit():
                continue
            if x > 0:
                if input[y][x-1].isdigit():
                    continue
            # get total number
            value_str = re.search('\d+', input[y][x:]).group()
            value = int(value_str)
            # add digit
            digits.add((x, y, value, value_str, x-1, x+len(value_str), y-1, y+1))
    
    score = 0
    for gear_x, gear_y in gears:
        close_digits = [dig[2] for dig in digits if dig[4] <= gear_x <= dig[5] and dig[6] <= gear_y <= dig[7]]
        
        if len(close_digits) == 2:
            score += math.prod(close_digits)
            print(gear_x, gear_y, math.prod(close_digits))
            

    return score

        


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    # part_one(lines)
    part_two(lines)
