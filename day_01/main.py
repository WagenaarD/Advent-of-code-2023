"""
Advent of code challenge 2023
>> python3 main.py < in
Start   - forgot
Part 1  - forgot
Part 2  - forgot
Cleanup - forgot
"""

import sys
sys.path.insert(0, '/'.join(__file__.replace('\\', '/').split('/')[:-2]))
from _utils.print_function import print_function
import re

NUMBER_LUT = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def clean_number_str(number: str) -> str:
    if number in NUMBER_LUT:
        return str(NUMBER_LUT.index(number) + 1)
    else:
        return number

@print_function()
def part_one(lines: 'list[str]') -> int:
    num_lines = [re.findall('\d', line) for line in lines]
    values = [int(nums[0] + nums[-1]) for nums in num_lines]
    return sum(values)

@print_function()
def part_two(lines: 'list[str]') -> int:
    num_lines = [re.findall('(?=(\d|' + '|'.join(NUMBER_LUT) + '))', line) for line in lines]
    values = [int(clean_number_str(nums[0]) + clean_number_str(nums[-1])) for nums in num_lines]
    return sum(values)
    
if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)

    # or alternatively as one liners:
    print('part 1:', sum([int(nums[0] + nums[-1]) for line in lines if (nums := re.findall('\d', line))]))
    print('part 2:', sum([int((nums[0] if nums[0].isdigit() else str(NUMBER_LUT.index(nums[0]) + 1)) + (nums[-1] if nums[-1].isdigit() else str(NUMBER_LUT.index(nums[-1]) + 1))) for line in lines if (nums := re.findall('(?=(\d|' + '|'.join(NUMBER_LUT) + '))', line))]))
