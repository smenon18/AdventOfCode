

def main() -> None:
    """
    Day fifteen of Advent of Code 2022
    :return: None
    """
    file = open('./input/dayFifteen.txt', 'r')
    grid: dict[tuple[int, int], str] = {}
    for line in file.read().split('\n'):
        x, y = int(line[12: line.index(',')]), int(line[line.index('y') + 2: line.index(':')])
        grid[x, y] = 'S'
        x, y = int(line[line.rindex('x') + 2: line.rindex(',')]), int(line[line.rindex('y') + 2:])
        grid[x, y] = 'B'
    print(grid)


if __name__ == "__main__":
    main()
