

def main():
    """
    Day Three Problem for Advent Of Code 2022
    :return:
    """
    file = open('./input/dayThree.txt', "r")
    rucksacks = [x for x in file.read().split("\n")]
    file.close()
    sum_a = 0
    sum_b = 0
    elves_group = []
    for ruck in rucksacks:
        a, b = ruck[:len(ruck)//2], ruck[len(ruck)//2:]
        dup = ''.join(set(a).intersection(b))
        prio = ord(dup.lower()) - ord('a') + 1 + (26 if dup.isupper() else 0)
        sum_a += prio
        elves_group.append(ruck)
        if len(elves_group) == 3:
            grp_dup = ''.join(set(elves_group[0]).intersection(elves_group[1], elves_group[2]))
            grp_prio = ord(grp_dup.lower()) - ord('a') + 1 + (26 if grp_dup.isupper() else 0)
            sum_b += grp_prio
            elves_group = []
    print("Part A:")
    print(sum_a)
    print("Part B:")
    print(sum_b)


if __name__ == "__main__":
    main()
