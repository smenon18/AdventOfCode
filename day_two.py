

def main():
    """
    Day 2 of Advent Of Code 2022
    :return: None
    """
    score_sheet_a = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    score_sheet_b = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
    running_score_a = 0
    running_score_b = 0
    file = open('./input/dayTwo.txt', "r")
    for strat in file.read().split("\n"):
        running_score_a += score_sheet_a[strat]
        running_score_b += score_sheet_b[strat]
    file.close()
    print("Part A:")
    print(running_score_a)
    print("Part B:")
    print(running_score_b)


if __name__ == "__main__":
    main()
