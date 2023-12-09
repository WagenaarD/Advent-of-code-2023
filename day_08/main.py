"""
Advent of code challenge 2023
python3 ../_utils/get_aoc_in.py
python3 main.py < in
"""
# Start, Part 1, Part 2
# 09:23:08
# 09:31:06
# 11:16:57

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from aoc_tools import print_function
import itertools as it
import re
from functools import reduce
import math

AOC_ANSWER = (16579, 12927600769609)

def part_one(lines):
    dirs = lines[0]
    words = [re.findall('\w+', line) for line in lines[2:]]
    elements = {word[0]: {'L': word[1], 'R': word[2]} for word in words}
    pos = 'AAA'
    for step_count, dir in enumerate(it.cycle(dirs)):
        if pos == 'ZZZ':
            break
        pos = elements[pos][dir]
    return step_count

def part_two(lines):
    dirs = lines[0]
    words = [re.findall('\w+', line) for line in lines[2:]]
    elements = {word[0]: {'L': word[1], 'R': word[2]} for word in words}
    pos = [key for key in elements if key.endswith('A')]
    z_found = [False for _ in pos]
    for step_count, dir in enumerate(it.cycle(dirs), 1):
        pos = [elements[p][dir] for p in pos]
        for idx, p in enumerate(pos):
            if p[-1] == 'Z' and not z_found[idx]:
                z_found[idx] = step_count
        if all(z_found):
            break
    return reduce(math.lcm, z_found)

@print_function()
def main(input: str) -> 'tuple(int, int)':
    lines = input.split('\n')
    return (part_one(lines), part_two(lines))


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    input = sys.stdin.read().strip()
    print('  ->', main(input) == (AOC_ANSWER[0], AOC_ANSWER[1]))
