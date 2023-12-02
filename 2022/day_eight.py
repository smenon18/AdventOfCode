

def main() -> None:
    """
    Day Eight Problem for Advent Of Code 2022
    :return:
    """
    def last(l: list) -> object:
        return l[-1]

    test = lambda l: l[-1]
    
    file = open('input/dayEight.txt', 'r')
    lines = file.read().splitlines()
    file.close()
    trees = {(x, y): int(h) for y, row in enumerate(lines) for x, h in enumerate(list(row))}
    visible = [(0, 0), (0, len(list(lines))), (len(lines), 0), (len(lines), len(list(lines)))]

    x_range = range(1, len(lines)-1)
    y_range = range(1, len(list(lines)) - 1)

    for y in y_range:  # left -> right
        visible.append((0, y))
        for x in x_range:
            if trees.get((x, y)) > trees.get(last(visible)):
                visible.append((x, y))
    for x in x_range:  # top -> bot
        visible.append((x, 0))
        for y in y_range:
            if trees.get((x, y)) > trees.get(last(visible)):
                visible.append((x, y))
    for y in y_range:  # right -> left
        visible.append((max(x_range) + 1, y))
        for x in reversed(x_range):
            if trees.get((x, y)) > trees.get(last(visible)):
                visible.append((x, y))
    for x in x_range:  # bot -> top
        visible.append((x, max(y_range) + 1))
        for y in reversed(y_range):
            if trees.get((x, y)) > trees.get(last(visible)):
                visible.append((x, y))
    print("Part A:")
    print(len(set(visible)))

    score = {(x, y): 0 for y, row in enumerate(lines) for x, _ in enumerate(list(row))}
    for x, y in trees.keys():
        if x == 0 or x == len(list(lines)) or y == 0 or y == len(lines):
            continue
        l_r = r_l = t_b = b_t = 0
        for x_v in range(x + 1, len(list(lines))):  # left -> right
            l_r += 1
            if trees.get((x_v, y)) >= trees.get((x, y)):
                break
        for y_v in range(y + 1, len(lines)):  # top -> bot
            t_b += 1
            if trees.get((x, y_v)) >= trees.get((x, y)):
                break
        for x_v in range(x - 1, -1, -1):  # right -> left
            r_l += 1
            if trees.get((x_v, y)) >= trees.get((x, y)):
                break
        for y_v in range(y - 1, -1, -1):  # bot -> top
            b_t += 1
            if trees.get((x, y_v)) >= trees.get((x, y)):
                break
        score.update({(x, y): l_r * t_b * r_l * b_t})
    print("Part B:")
    print(sorted(score.values())[-1])


if __name__ == '__main__':
    main()
