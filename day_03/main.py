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
def part_one(lines: 'list[str]'):
    """My attempt at a Jonathon Paulson type solution"""
    score = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            # if not the start of a number, ignore this cell
            if not char.isdigit():
                continue
            if x > 0 and line[x-1].isdigit():
                continue
            # get total number
            value_str = re.search('\d+', line[x:]).group()
            value = int(value_str)
            # check if adjacent to any symbol
            adjacent_symbol = False
            for yy in range(max(0, y-1), min(len(lines), y+2)):
                for xx in range(max(0, x-1), min(len(line), x+len(value_str)+1)):
                    if lines[yy][xx].isdigit() or lines[yy][xx] == '.':
                        pass
                    else:
                        adjacent_symbol = True
            if adjacent_symbol:
                score += value
    return score
            
@print_function()
def part_two(input: 'list[str]'):
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

    return score

@print_function()
def main(lines):
    """My attempt at a LiquidFun type solution"""
    grid = [(x, y, char) for y, line in enumerate(lines) for x, char in enumerate(line)]
    symbols = [(x, y, char) for (x, y, char) in grid if char != '.' and not char.isdigit()]
    stars = [(x, y, char) for (x, y, char) in grid if char == '*']
    digits = [(match.start(), y, match.group()) for y, line in enumerate(lines) for match in re.finditer('\d+', line)]
    in_range = lambda d, g: d[0]-1 <= g[0] <= d[0] + len(d[2]) and d[1]-1 <= g[1] <= d[1]+1
    part_one = sum([int(dig[2]) for dig in digits if any([in_range(dig, sym) for sym in symbols])])
    gear_nums = [[int(dig[2]) for dig in digits if in_range(dig, star)] for star in stars]
    part_two = sum([math.prod(nums) for nums in gear_nums if len(nums) == 2])
    return(part_one, part_two)


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

    main(lines)
