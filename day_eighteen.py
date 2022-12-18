from typing import Set


def main() -> None:
    """
    Day Eighteen problem for Advent of Code 2022
    :return: None
    """
    file = open('./input/dayEighteen.txt', 'r')
    lava: set[tuple[int, int, int]] = set()
    for line in file.read().split('\n'):
        x, y, z = line.split(',')
        lava.add((int(x), int(y), int(z)))
    file.close()
    sides_alone = 0
    for x, y, z in lava:
        if (x+1, y, z) not in lava:
            sides_alone += 1
        if (x-1, y, z) not in lava:
            sides_alone += 1
        if (x, y+1, z) not in lava:
            sides_alone += 1
        if (x, y-1, z) not in lava:
            sides_alone += 1
        if (x, y, z+1) not in lava:
            sides_alone += 1
        if (x, y, z-1) not in lava:
            sides_alone += 1
    print('Part A:')
    print(sides_alone)

if __name__ == '__main__':
    main()
