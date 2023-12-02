

def main():
    """"
    First Problem for Advent Of Code 2022
    :return: none
    """
    file = open('input/dayOne.txt', "r")
    elves = [[int(line) for line in block.split("\n")] for block in file.read()[:-1].split("\n\n")]
    file.close()
    print("Part 1: ")  # find highest cal count
    print(max(sum(e) for e in elves))
    print("Part 2: ")  # find sum of 3 highest cal count
    print(sum(sorted([sum(e) for e in elves])[-3:]))


if __name__ == '__main__':
    main()
