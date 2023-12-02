

def main():
    """
    Day Four Problem for Advent Of Code 2022
    :return: None
    """
    file = open('input/dayFour.txt', "r")
    elf_pairs = [[i for i in x.split(",")] for x in file.read().split("\n")]
    file.close()
    part_overlap = 0
    full_overlap = 0
    for pair in elf_pairs:
        e1 = [int(i) for i in pair[0].split("-")]
        e2 = [int(i) for i in pair[1].split("-")]
        print(e1, e2)
        if e1[0] >= e2[0] and e1[1] <= e2[1]:
            full_overlap += 1
        elif e1[0] <= e2[0] and e1[1] >= e2[1]:
            full_overlap += 1
        if e2[0] <= e1[0] <= e2[1] or e1[0] <= e2[0] <= e1[1]:
            part_overlap += 1
    print("Part A: ")
    print(full_overlap)
    print("Part B: ")
    print(part_overlap)


if __name__ == "__main__":
    main()
