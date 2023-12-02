import re


def main():
    """
    Day 1 Advent of Code 2023
    :return: none
    """
    part_1_sum = 0
    part_2_sum = 0
    VALUES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    VAL_DICT = {VALUES[i]: str(i) for i in range(len(VALUES))}
    file = open('input/dayOne.txt', "r")
    for line in file.read().split("\n"):
        digits = re.findall(r"\d", line)
        part_1_sum += int(digits[0] + digits[-1])
    print("Part 1: " + str(part_1_sum))
    file.close()
    file = open('input/dayOne.txt', "r")
    for line in file.read().split("\n"):
        digits = re.findall(r'(?=(' + '|'.join(VALUES) + "|\d" + '))', line)
        if len(digits[0]) > 1:
            digits[0] = VAL_DICT[digits[0]]
        if len(digits[-1]) > 1:
            digits[-1] = VAL_DICT[digits[-1]]
        part_2_sum += int(digits[0] + digits[-1])
    print("Part 2: " + str(part_2_sum))


if __name__ == '__main__':
    main()
