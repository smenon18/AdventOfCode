def main() -> None:
    """
    Advent of Code Day 5 Solution
    :return: None
    """
    with open('input/dayFive.txt', 'r') as file:
        lines = file.readlines()
        seeds = [int(seed) for seed in lines[0].split(":")[1][1:].split()]
        seeds_2 = []
        for i in range(0, len(seeds), 2):
            for j in range(seeds[i+1] + 1):
                seeds_2.append(seeds[i] + j)
        modified_loc = [False] * len(seeds)
        for line in lines[2:]:
            if not line.strip().endswith(":") or len(line.strip()) == 0:
                vals = [int(val) for val in line.split()]
                if len(vals) == 0:
                    continue
                for i in range(len(seeds)):
                    if not modified_loc[i] and vals[1] <= seeds[i] < vals[1] + vals[2]:
                        seeds[i] = vals[0] + seeds[i] - vals[1]
                        modified_loc[i] = True
            else:
                modified_loc = [False] * len(seeds)
        for start, length in zip(*[iter(seeds)] * 2):
            s_range = [(start, start + length - 1)]
            d_range = []
            
        print('Part 1:', min(seeds))
        print('Part 2:', min(seeds_2))


if __name__ == "__main__":
    main()
