from copy import deepcopy
from typing import TypeAlias


Cave: TypeAlias = dict[tuple[int, int]: str]


def main() -> None:
    """
    Day 14 problem for Advent of Code 2022
    :return: None
    """
    file = open('./input/dayFourteen.txt', 'r')
    cave: Cave = {}
    for line in file.read().split('\n'):
        coords = line.split('->')
        p = coords.pop(0).strip().split(',')
        px = int(p[0])
        py = int(p[1])
        while len(coords) != 0:
            n = coords.pop(0).strip().split(',')
            nx = int(n[0])
            ny = int(n[1])
            c = 'x'
            if px > nx:
                r = range(nx, px + 1)
            elif px < nx:
                r = range(px, nx + 1)
            elif py > ny:
                r = range(ny, py + 1)
                c = 'y'
            else:
                r = range(py, ny + 1)
                c = 'y'
            for i in r:
                if c == 'x':
                    cave[(i, py)] = '#'
                else:
                    cave[(px, i)] = '#'
            px, py = nx, ny
    file.close()
    sand_start = (500, 0)
    min_x, max_x = min(p[0] for p in cave.keys()), max(p[0] for p in cave.keys())
    min_y, max_y = min(p[1] for p in cave.keys()), max(p[1] for p in cave.keys())
    cave_b = deepcopy(cave)
    settled_sand = 0
    overflow = False
    curr = sand_start
    cave[curr] = '+'
    while not overflow:
        settled = False
        while not settled:
            if not min_x <= curr[0] <= max_x or not curr[1] <= max_y:
                cave[curr] = None
                overflow = True
                break
            if not (curr[0], curr[1] + 1) in cave.keys() or cave[curr[0], curr[1] + 1] is None:
                cave[curr], cave[curr[0], curr[1] + 1] = None, cave[curr]
                curr = (curr[0], curr[1] + 1)
            elif not (curr[0] - 1, curr[1] + 1) in cave.keys() or cave[curr[0] - 1, curr[1] + 1] is None:
                cave[curr], cave[curr[0] - 1, curr[1] + 1] = None, cave[curr]
                curr = (curr[0] - 1, curr[1] + 1)
            elif not (curr[0] + 1, curr[1] + 1) in cave.keys() or cave[curr[0] + 1, curr[1] + 1] is None:
                cave[curr], cave[curr[0] + 1, curr[1] + 1] = None, cave[curr]
                curr = (curr[0] + 1, curr[1] + 1)
            else:
                settled = True
                settled_sand += 1
                curr = sand_start
                cave[curr] = '+'
    print('Part A:')
    print(settled_sand)
    for i in range(min_x - 1000, max_x + 1001):
        cave_b[(i, max_y + 2)] = '#'
    min_x -= 1000
    max_x += 1000
    settled_sand_b = 0
    curr = sand_start
    while sand_start not in cave_b.keys() or not cave_b[sand_start] == '+':
        settled = False
        cave_b[curr] = '+'
        while not settled:
            if not (curr[0], curr[1] + 1) in cave_b.keys() or cave_b[curr[0], curr[1] + 1] is None:
                cave_b[curr], cave_b[curr[0], curr[1] + 1] = None, cave_b[curr]
                curr = (curr[0], curr[1] + 1)
            elif not (curr[0] - 1, curr[1] + 1) in cave_b.keys() or cave_b[curr[0] - 1, curr[1] + 1] is None:
                cave_b[curr], cave_b[curr[0] - 1, curr[1] + 1] = None, cave_b[curr]
                curr = (curr[0] - 1, curr[1] + 1)
            elif not (curr[0] + 1, curr[1] + 1) in cave_b.keys() or cave_b[curr[0] + 1, curr[1] + 1] is None:
                cave_b[curr], cave_b[curr[0] + 1, curr[1] + 1] = None, cave_b[curr]
                curr = (curr[0] + 1, curr[1] + 1)
            else:
                settled = True
                settled_sand_b += 1
                curr = sand_start
    print('Part B:')
    print(settled_sand_b)


if __name__ == '__main__':
    main()
