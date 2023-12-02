from copy import deepcopy


def main() -> None:
    """
    Day eleven problem for Advent of code 2022
    :return: None
    """
    file = open('input/dayEleven.txt', 'r')
    monkeys = []
    for chunk in file.read().split('\n\n'):
        num = 0
        items = []
        op = None
        divisible_by = 0
        true_monk, false_monk = 0, 0
        c = 0
        for line in chunk.splitlines():
            line = line.strip()
            if line.startswith('Monkey'):
                num = int(line.split()[1][0])
            elif line.startswith('Starting items'):
                line = line[15:]
                items = [int(i) for i in line.split(',')]
            elif line.startswith('Operation'):
                line = line[20:]
                if line.split()[1] == 'old':
                    op = lambda v, n: pow(v, 2)
                elif line.split()[0] == '+':
                    op = lambda v, n: v + n
                    c = int(line.split()[1])
                else:
                    op = lambda v, n: v * n
                    c = int(line.split()[1])
            elif line.startswith('Test'):
                line = line[19:]
                divisible_by = int(line)
            elif line.startswith('If true'):
                true_monk = int(line.split()[-1])
            else:
                false_monk = int(line.split()[-1])
        monkeys.append({'id': num, 'items': items, 'operation': op, 'divisible_by': divisible_by,
                        'True': true_monk, 'False': false_monk, 'c': c, 'interactions': 0})
    file.close()
    monkeys_b = deepcopy(monkeys)
    for i in range(20):
        for curr_monk in monkeys:
            curr_op = curr_monk['operation']
            while len(curr_monk['items']) > 0:
                curr_item = curr_monk['items'].pop(0)
                curr_monk['interactions'] += 1
                curr_item = curr_op(curr_item, curr_monk['c'])
                curr_item //= 3
                monkeys[curr_monk[str(curr_item % curr_monk['divisible_by'] == 0)]]['items'].append(curr_item)
    print('Part A:')
    monkey_business = sorted([m['interactions'] for m in monkeys])
    print(monkey_business[-2] * monkey_business[-1])
    limiter = 1
    for m in monkeys_b:
        limiter *= m['divisible_by']  # lcm in python 3.9+
    for i in range(10_000):
        for curr_monk in monkeys_b:
            curr_op = curr_monk['operation']
            while len(curr_monk['items']) > 0:
                curr_item = curr_monk['items'].pop(0)
                curr_monk['interactions'] += 1
                curr_item = curr_op(curr_item, curr_monk['c'])
                curr_item %= limiter
                monkeys_b[curr_monk[str(curr_item % curr_monk['divisible_by'] == 0)]]['items'].append(curr_item)
    print('Part B:')
    monkey_business_b = sorted([m['interactions'] for m in monkeys_b])
    print(monkey_business_b[-2] * monkey_business_b[-1])


if __name__ == '__main__':
    main()
