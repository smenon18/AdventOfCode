def main() -> None:
    """
    Advent Of Code 2023 Day 9  Solution
    :return: None
    """
    sum = 0
    back_sum = 0
    with open('input/dayNine.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        vals = [int(v) for v in line.split()]
        differences = [[]]
        prev = vals[0]
        for val in vals[1:]:
            differences[0].append(val - prev)
            prev = val
        while not set(differences[-1]) == {0}:
            d_vals = differences[-1]
            prev = d_vals[0]
            next_diffs = []
            for val in d_vals[1:]:
                next_diffs.append(val - prev)
                prev = val
            differences.append(next_diffs)
        count = 0
        back = 0
        for diff_list in reversed(differences):
            count += diff_list[-1]
            back = diff_list[0] - back
        sum += (count + vals[-1])
        back_sum += (vals[0] - back)
    print('Part 1:', sum)
    print('Part 2:', back_sum)


if __name__ == '__main__':
    main()
