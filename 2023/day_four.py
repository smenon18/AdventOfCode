from collections import defaultdict


def main() -> None:
    """
    Advent Of Code Day 4
    :return: None
    """
    sum_points = 0
    num_next = {1: 1}
    with open('input/dayFour.txt', 'r') as file:
        for line in file:
            card_num = int(line.split(':')[0].split()[1])
            if card_num not in num_next.keys():
                num_next[card_num] = 1
            line = line.split(':')[1]
            data = line.split('|')
            winning_nums = set(data[0].split())
            line_pts = 0
            num_matches = 0
            for num in data[1].split():
                if num in winning_nums:
                    num_matches += 1
                    if line_pts == 0:
                        line_pts = 1
                    else:
                        line_pts = line_pts << 1
            sum_points += line_pts
            for match in range(1, num_matches + 1):
                num_next[card_num + match] = num_next.get(card_num + match, 1) + num_next.get(card_num)
        print('Part 1:', sum_points)
        print('Part 2:', sum(val for val in num_next.values()))


if __name__ == '__main__':
    main()
