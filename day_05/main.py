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


@print_function()
def main(lines):
    seeds = map(int, re.findall('\d+', lines[0]))
    luts = []
    for line in lines[1:]:
        if line == '':
            continue
        elif not line[0].isdigit():
            luts.append([])
        else:
            luts[-1].append([int(num) for num in re.findall('\d+', line)])
    # print(luts[0])
    p1 = []
    for pos in seeds:
        # print(pos)
        for lut in luts:
            for dst, src, lng in lut:
                if src <= pos < src + lng :
                    pos = dst + (pos - src)
                    # print('  y', dst, src, lng)
                    break
                # else:
                    # print('   n', dst, src, lng)
            # print(pos)
        # print('=' * 16)
        p1.append(pos)
    print(p1)
    return min(p1)

    

if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    print('\n'.join(lines))
    # input = sys.stdin.read().strip()
    main(lines)

