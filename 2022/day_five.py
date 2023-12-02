from copy import deepcopy


def main():
    """
    Day Five Problem for Advent Of Code 2022
    :return: None
    """
    file = open('input/dayFive.txt', "r")
    parts = [i for i in file.read().split("\n\n")]
    stacks = [[] for _ in range(9)]
    for line in reversed(list(parts[0].splitlines())):
        if line.strip().startswith("["):
            counter = 0
            while line != '':
                if line[0:3].strip() != '':
                    stacks[counter].append(line[1:2].strip())
                line = line[4:]
                counter += 1
    instructions = [[int(i.rsplit(" ")[1]), int(i.rsplit(" ")[3]), int(i.rsplit(" ")[5])] for i in parts[1].split("\n")]
    file.close()
    stacks_a = deepcopy(stacks)  # create a copy to do both parts
    for c, f, t in instructions:
        move = []
        for _ in range(c):
            stacks_a[t - 1].append(stacks_a[f - 1].pop())  # Part A : move 1 at a time
            move.append(stacks[f-1].pop())
        while not len(move) == 0:
            stacks[t-1].append(move.pop())
    print("Part A:")
    ans_a = ""
    for s in stacks_a:
        ans_a += s[len(s) - 1]
    print(ans_a)
    print("Part B:")
    ans_b = ""
    for s in stacks:
        ans_b += s[len(s) - 1]
    print(ans_b)


if __name__ == "__main__":
    main()
