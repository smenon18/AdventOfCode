import math


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
        min = min_dists[i]
        time = times[i]
        #do math
        dis = math.sqrt(time ** 2 - 4 * (-1) * (-min))
        x1 = math.floor((time + dis) / (2 * (-1)))
        x2 = math.ceil((time - dis) / (2 * (-1))) - 1
        mul *= abs(x2 - x1)
    print('Part 1:', mul)
    dis = math.sqrt(big_time ** 2 - 4 * (-1) * (-big_dist))
    x1 = math.floor((big_time + dis) / (2 * (-1)))
    x2 = math.ceil((big_time - dis) / (2 * (-1))) - 1
    print('Part 2:', abs(x2 - x1))


if __name__ == "__main__":
    main()
