import math


def calc(a, b, c) -> int:
    dis = math.sqrt(b ** 2 - 4 * a * c)
    x1 = math.floor((b + dis) / 2 * a)
    x2 = math.ceil((b - dis) / 2 * a) - 1
    return abs(x2 - x1)


def main() -> None:
    """
    Advent of Code day 6 solution
    :return: None
    """
    with open('input/daySix.txt', 'r') as file:
        lines = file.readlines()
    times = [int(val) for val in lines[0].split(":")[1].strip().split()]
    big_time = int("".join(lines[0].split(":")[1].strip().split()))
    min_dists = [int(val) for val in lines[1].split(":")[1].strip().split()]
    big_dist = int("".join(lines[1].split(":")[1].strip().split()))
    mul = 1
    for i in range(len(times)):
        mul *= calc(-1, times[i], -min_dists[i])
    print('Part 1:', mul)
    print('Part 2:', calc(-1, big_time, -big_dist))


if __name__ == "__main__":
    main()
