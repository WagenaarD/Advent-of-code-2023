import os
import importlib
from aoc_tools import print_function


@print_function()
def run_all(aoc_path):
    for day_name in sorted(os.listdir()):
        if not day_name.startswith('day_') or day_name.endswith('0'):
            continue
        print('\n', day_name)
        with open(f'{day_name}/in') as f:
            input = f.read().strip()
        code = importlib.import_module(f'{day_name}.main')
        print(code.main(input) == code.AOC_ANSWER)


if __name__ == '__main__':
    """Executed if file is executed but not if file is imported."""
    script_path = '/'.join(__file__.replace('\\', '/').split('/')[:-1])
    run_all(script_path)