

def m_dist(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # |x1-x2|+|y1-y2|


def main() -> None:
    """
    Day fifteen of Advent of Code 2022
    :return: None
    """
    file = open('./input/dayFifteen.txt', 'r')
    limit = 2000000
    beacons: set[int] = set()  # keep set of beacons and signals to remove from other set at end
    beaconless: set[int] = set()
    sensors: dict[tuple[int, int], int] = {}
    for line in file.read().split('\n'):
        sx, sy = int(line[12: line.index(',')]), int(line[line.index('y') + 2: line.index(':')])
        bx, by = int(line[line.rindex('x') + 2: line.rindex(',')]), int(line[line.rindex('y') + 2:])
        dist = m_dist((sx, sy), (bx, by))
        sensors[sx, sy] = dist
        if limit == by:
            beacons.add(bx)
        if limit == sy:
            beacons.add(sx)  # \/ lower  and upper bound of scanned area with limit as y
        beaconless |= set(range(sx - dist + abs(limit - sy), sx + dist - abs(limit - sy) + 1))
    beaconless -= beacons
    print('Part A:')
    print(len(beaconless))
    max_xy = 4000000
    for s_point, dist in sensors.items():
        sx, sy = s_point  # create ranges with this that mimics the data passed into set union from p1
        for i in range(max(0, sx-dist-1), min(max_xy, sx + dist + 2)):
            for j in [sy + (dist + 1 - abs(i - sx)), sy - (dist + 1 - abs(i - sx))]:
                if j in range(max_xy + 1):
                    for s_p2, d2 in sensors.items():
                        if m_dist((i, j), s_p2) <= d2:
                            break
                    else:
                        print('Part B:')
                        print(i * max_xy + j)
                        return  # would be better to make this loop seq a function and return printed line above


if __name__ == "__main__":
    main()
