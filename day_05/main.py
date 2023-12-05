"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - 
Part 1  - 
Part 2  - 
Cleanup - 
"""
# 08:02:04
# 08:32:37
# 

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

NAMES = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]
INF = 1_000_000_000_000

@print_function()
def part_one(lines):
    seeds = map(int, re.findall('\d+', lines[0]))
    luts = []
    for line in lines[1:]:
        if line == '':
            continue
        elif not line[0].isdigit():
            luts.append([])
        else:
            luts[-1].append([int(num) for num in re.findall('\d+', line)])
    p1 = []
    for pos in seeds:
        for lut in luts:
            for dst, src, lng in lut:
                if src <= pos < src + lng :
                    pos = dst + (pos - src)
                    break
        p1.append(pos)
    print(p1)
    return min(p1)

@print_function()
def part_two(lines):
    seed_ranges = [tuple(map(int, pair.split())) for pair in re.findall('\d+ \d+', lines[0])]
    seed_ranges = {(start, start + length - 1) for start, length in seed_ranges}

    luts = []
    for line in lines[1:]:
        if line == '':
            continue
        elif not line[0].isdigit():
            luts.append([])
        else:
            dst, lut_start, lut_len = [int(num) for num in re.findall('\d+', line)]
            luts[-1].append((lut_start, lut_start + lut_len - 1, dst - lut_start))
    for lut in luts:
        lut.sort(key = lambda x: x[0])
        # Verfy no overlap: the end of current lut <= start of next lut
        for idx in range(len(lut) - 1):
            assert lut[idx][1] <= lut[idx+1][0], 'Overlapping lut'
    
    # seed        82
    # soil        84
    # fertilizer  84
    # water       84
    # light       77
    # temperature 45
    # humidity    46
    # location    46
    for lut_idx, lut in enumerate(luts):
        print('='*6, NAMES[lut_idx], '='*6)
        print('seed_ranges', seed_ranges)
        lut_nodes = [-1, INF] + [l[0] for l in lut] + [l[1] for l in lut]
        print('lut', lut)
        print('lut_nodes', lut_nodes)
        next_seed_ranges = set()
        for seed_start, seed_end in seed_ranges:
            nodes = sorted(list(set(lut_nodes + [seed_start, seed_end + 1])))
            # print('nodes', nodes)
            for node, next_node in zip(nodes, nodes[1:]):
                offset = 0
                node_in_seed = seed_start <= node <= seed_end
                # print('(node, next_node-1, node_in_seed):', (node, next_node-1, node_in_seed))
                if not node_in_seed:
                    continue
                for lut_start, lut_end, lut_offset in lut:
                    node_in_lut = lut_start <= node <= lut_end
                    if node_in_lut:
                        offset = lut_offset
                        break
                next_seed_ranges.add((node + offset, next_node + offset - 1))
        seed_ranges = next_seed_ranges
    print(seed_ranges)
    return min([num[0] for num in seed_ranges])
                

    
    return

    p1 = []

    once = False
    for idx, lut in enumerate(luts):
        new_seed_ranges = set()
        print('='*6, NAMES[idx], '='*6)
        print(seed_ranges)
        # for seed_start, seed_len in seed_ranges:
        action = False
        old_seed_ranges = set()
        planned_seed_ranges = seed_ranges.copy()
        while seed_ranges:
            # if seed_ranges != old_seed_ranges:
            #     print(seed_ranges, old_seed_ranges)
            #     old_seed_ranges = seed_ranges.copy()
            # else:
            #     print('', '?'*8)
            #     print('', new_seed_ranges)
            #     print('', seed_start, seed_len)
            #     print('', lut[0])
            #     dst, lut_start, lut_len = lut[0]
            #     lut_end = lut_start + lut_len - 1
            #     print('', seed_start <= lut_end, seed_end <= lut_end)
            #     exit()

            seed_start, seed_len = seed_ranges.pop()
            seed_end = seed_start + seed_len - 1
            
            
            # if seed_start == 77:
            #     if not once:
            #         once = True
            #     else:
            #         print('?'*8)
            #         print(new_seed_ranges)
            #         print('', seed_start, seed_len)
            #         print(lut[0])
            #         dst, lut_start, lut_len = lut[0]
            #         lut_end = lut_start + lut_len - 1
            #         print(seed_start <= lut_end, seed_end <= lut_end)
            #         exit()
            # if all(seed_end < lut_start or seed_start > (lut_start + lut_len - 1) for dst, lut_start, lut_len in lut):
            #     new_seed_ranges.add((seed_start, seed_len))
            #     continue
            for dst, lut_start, lut_len in lut:
                offset = dst - lut_start
                lut_end = lut_start + lut_len - 1
                if seed_start < lut_start:
                    if seed_end < lut_start:
                        # Seed is outside of LUT range, do nothing
                        #  seed |----|
                        #  lut         |----|
                        pass
                        print(1)
                        # seed_ranges.add((seed_start, seed_len))
                    elif seed_end <= lut_end:
                        #  seed     |----|
                        #  lut         |----|
                        print(2)
                        new_seed_range_plan = (seed_start, lut_start - seed_start + 1)
                        if not new_seed_range_plan in planned_seed_ranges:
                            planned_seed_ranges.add(new_seed_range_plan)
                            seed_ranges.add(new_seed_range_plan)
                        new_seed_ranges.add((lut_start + offset, seed_end - lut_start + 1))
                        action = True
                    else: # seed_end > lut_end
                        #  seed     |----------|
                        #  lut         |----|
                        print(3)
                        new_seed_range_plan = (seed_start, lut_start - seed_start + 1)
                        if not new_seed_range_plan in planned_seed_ranges:
                            planned_seed_ranges.add(new_seed_range_plan)
                            seed_ranges.add(new_seed_range_plan)
                        new_seed_ranges.add((lut_start + offset, lut_len))
                        new_seed_range_plan = (lut_end + 1, seed_end - (lut_end + 1) + 1)
                        if not new_seed_range_plan in planned_seed_ranges:
                            planned_seed_ranges.add(new_seed_range_plan)
                            seed_ranges.add(new_seed_range_plan)
                        action = True
                elif seed_start <= lut_end:
                    if seed_end < lut_start:
                        assert False, 'seed_start > lut_start but seed_end < lut_start..., so seed_end < seed_start?'
                    elif seed_end <= lut_end:
                        #  seed         |--|
                        #  lut         |----|
                        print(4)
                        new_seed_ranges.add((seed_start + offset, seed_len))
                        action = True
                    else: # seed_end > lut_end
                        #  seed          |----|
                        #  lut         |----|
                        print(5)
                        new_seed_ranges.add((seed_start + offset, lut_end - seed_start + 1))
                        new_seed_range_plan = (lut_end + 1, seed_end - (lut_end + 1) + 1)
                        if not new_seed_range_plan in planned_seed_ranges:
                            planned_seed_ranges.add(new_seed_range_plan)
                            seed_ranges.add(new_seed_range_plan)
                        action = True
                else: # seed_start > lut_end:
                    # Seed is outside of LUT range, do nothing
                    #  seed               |----|
                    #  lut         |----|
                    pass
                    print(6)
                    # seed_ranges.add((seed_start, seed_len))
            if not action:
                # seed_ranges.remove((seed_start, seed_len))
                new_seed_ranges.add((seed_start, seed_len))
        seed_ranges = new_seed_ranges
    print(seed_ranges)
    return min([num[0] for num in seed_ranges])

    

if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    # print('\n'.join(lines))
    # part_one(lines)
    part_two(lines)
    # part_two(['seeds: 79 14'] + lines[1:])
    # part_two(['seeds: 82 1'] + lines[1:])

