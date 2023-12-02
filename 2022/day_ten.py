

def exec_op(instructions):
    x = 1
    for inst in instructions:
        yield x
        if inst[0] == 'addx':
            yield x
            x += int(inst[1])


def main() -> None:
    """
    Day Ten Advent of Code problem
    :return: None
    """
    file = open('input/dayTen.txt', 'r')
    instructions = [line for line in file.read().splitlines()]
    file.close()
    signals = list(exec_op(inst.split() for inst in instructions))
    print("Part A:")
    print(sum(signals[i-1] * i for i in [20, 60, 100, 140, 180, 220]))
    print('Part B:')
    for i in range(6):
        print(''.join('.#'[abs(signals[i*40+j] - j) <= 1] for j in range(40)))


if __name__ == '__main__':
    main()
