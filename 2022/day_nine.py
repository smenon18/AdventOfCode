

def move_tail_many(head, tail) -> None:
    change_xy = [x - y for x, y in zip(head, tail)]  # changed to list dist between head tail 2 vals
    if abs(change_xy[0]) > 1 or abs(change_xy[1]) > 1:
        tail[:] = [n + (1 if change_n >= 1 else -1 if change_n <= -1 else 0) for n, change_n in zip(tail, change_xy)]


def main() -> None:
    """
    Day Nine Problem for Advent Of Code 2022
    :return:
    """
    file = open('input/dayNine.txt', 'r')
    lines = file.read().splitlines()
    file.close()
    movements = [(line.split()[0], int(line.split()[1])) for line in lines]
    offset = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    tail_visits = {(0, 0)}
    tail_visits_b = {(0, 0)}
    hx, hy = 0, 0
    h = [hx, hy]  # changed to list for easier typing / processing
    tx, ty = 0, 0
    tails = [[0, 0] for _ in range(9)]  # changed to list(list)) for easier processing
    for d, i in movements:
        dx, dy = offset[d]
        for _ in range(i):
            hx += dx
            hy += dy
            while max(abs(hx - tx), abs(hy - ty)) > 1:
                if abs(hx - tx) > 0:
                    tx += 1 if hx > tx else -1
                if abs(hy - ty) > 0:
                    ty += 1 if hy > ty else -1
                tail_visits.add((tx, ty))
    print("Part A:")
    print(len(tail_visits))
    for d, t in movements:
        for _ in range(t):
            h = [x + y for x, y in zip(h, offset[d])]
            for i in range(len(tails)):
                move_tail_many(h if i == 0 else tails[i - 1], tails[i])
                if i == 8:
                    tail_visits_b.add(tuple(tails[i]))
    print('Part B:')
    print(len(tail_visits_b))


if __name__ == '__main__':
    main()
