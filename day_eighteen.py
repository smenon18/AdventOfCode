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
    outside_surface = 0
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
        max_x = max(i[0] for i in lava if i[1] == y and i[2] == z)
        max_y = max(i[1] for i in lava if i[0] == x and i[2] == z)
        max_z = max(i[2] for i in lava if i[0] == x and i[1] == y)
        min_x = min(i[0] for i in lava if i[1] == y and i[2] == z)
        min_y = min(i[1] for i in lava if i[0] == x and i[2] == z)
        min_z = min(i[2] for i in lava if i[0] == x and i[1] == y)
        if x-1 < min_x:
            outside_surface += 1
        if x+1 > max_x:
            outside_surface += 1
        if y-1 < min_y:
            outside_surface += 1
        if y+1 > max_y:
            outside_surface += 1
        if z-1 < min_z:
            outside_surface += 1
        if z+1 > max_z:
            outside_surface += 1
    print('Part A:')
    print(sides_alone)
    print('Part B:')
    print(outside_surface)


if __name__ == '__main__':
    main()
