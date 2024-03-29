import re
from collections import defaultdict


SYMBOL_REGEX = re.compile('[@_!#$%^&*()<>?/\|}{~:+=`~-]')
NUMS_REGEX = re.compile('\d+')


def find_symbol(data, min_x, min_y, max_x, max_y) -> bool:
    for i in range(min_x, max_x+1):
        found = SYMBOL_REGEX.search(data[i][min_y:max_y])
        if found:
            return found
    return False


def main() -> None:
    """
    Advent of Code 2023 day 3
    :return: None
    """
    file = open('input/dayThree.txt', 'r')
    data = [line.strip() for line in file]
    file.close()
    gears = defaultdict(list)
    sum_part_nums = 0
    for idx, line in enumerate(data):
        for match in NUMS_REGEX.finditer(line):
            num = int(match.group())
            min_x = max(0, idx-1)
            min_y = max(0, match.start()-1)
            max_x = min(len(data)-1, idx+1)
            max_y = min(len(line)-1, match.end()+1)
            found = find_symbol(data, min_x, min_y, max_x, max_y)
            if found:
                sum_part_nums += int(match.group())
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y):
                    if data[x][y] == '*':
                        gears[(x, y)].append(num)
    print('Part 1:', sum_part_nums)
    sum_gear_ratio = 0
    for nums in gears.values():
        if len(nums) == 2:
            sum_gear_ratio += (nums[0] * nums[1])
    print('Part 2:', sum_gear_ratio)


if __name__ == '__main__':
    main()
