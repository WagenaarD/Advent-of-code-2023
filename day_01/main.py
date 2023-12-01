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
    # start_nums = [re.search('\d|' + '|'.join(NUMBER_LUT), line).group() for line in lines]
    # start_nums = [clean_number_str(num) for num in start_nums]
    # inverse_lut = [dig[::-1] for dig in NUMBER_LUT]
    # end_nums = [re.search('\d|' + '|'.join(inverse_lut), line[::-1]).group()[::-1] for line in lines]
    # end_nums = [clean_number_str(num) for num in end_nums]
    # values = [int(start + end) for start, end in zip(start_nums, end_nums)]
    num_lines = [re.findall('(?=(\d|' + '|'.join(NUMBER_LUT) + '))', line) for line in lines]
    values = [int(clean_number_str(nums[0]) + clean_number_str(nums[-1])) for nums in num_lines]
    return sum(values)
    
if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    lines = sys.stdin.read().strip().split('\n')
    part_one(lines)
    part_two(lines)