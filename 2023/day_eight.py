import math


def all_is_not_ended(nodes: list[str]) -> bool:
    for node in nodes:
        if not node.endswith('Z'):
            return True
    return False


def main() -> None:
    """
    Advent Of Code day eight
    :return: None
    """
    with open('input/dayEight.txt', 'r') as file:
        lines = file.readlines()
        moves = lines[0].strip()
        map = {}
        for line in lines[2:]:
            kv = line.strip().split('=')
            map[kv[0].strip()] = kv[1][2:-1].strip().split(', ')
        curr = 'AAA'
        steps = 0
        i = 0
        while curr != 'ZZZ':
            nodes = map.get(curr)
            if i >= len(moves):
                i = 0
            curr = nodes[0] if moves[i] == 'L' else nodes[1]
            steps += 1
            i += 1
        print('Part 1:', steps)
        starts = [key for key in map.keys() if key.endswith('A')]
        currs = starts
        steps_to_fin = [0 for i in range(len(starts))]
        steps = 0
        while all_is_not_ended(currs):
            if i >= len(moves):
                i = 0
            move = moves[i]
            for j, node in enumerate(currs):
                if not node.endswith('Z'):
                    nexts = map.get(node)
                    currs[j] = nexts[0] if move == 'L' else nexts[1]
            steps += 1
            i += 1
            for k, node in enumerate(currs):
                if node.endswith('Z') and steps_to_fin[k] == 0:
                    steps_to_fin[k] = steps

        print('Part 2:', math.lcm(*steps_to_fin))


if __name__ == '__main__':
    main()
