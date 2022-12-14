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
        print(p)
        px = int(p[0])
        py = int(p[1])
        while len(coords) != 0:
            n = coords.pop(0).strip().split(',')
            nx = int(n[0])
            ny = int(n[1])
            print(n)
            c = 'x'
            if px > nx:
                r = range(nx, px)
            elif px < nx:
                r = range(px,nx)
            elif py > ny:
                r = range(ny,py)
                c = 'y'
            else:
                r = range(py, ny)
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
    print(cave)
    print(min_x, max_x, sand_start, min_y, max_y)


if __name__ == '__main__':
    main()
