import functools


def hand_values(hand1: list, hand2: list) -> int:
    """
    Sort hands based on value and starting cards
    :param hand1:
    :param hand2:
    :return: int representing sort
    """
    freq_h1 = {}
    freq_h2 = {}
    ord_change = {'T': 58, 'J': 59, 'Q': 60, 'K': 61}
    for idx, i in enumerate(hand1[0]):
        if i in freq_h1:
            freq_h1[i] += 1
        else:
            freq_h1[i] = 1
        if hand2[0][idx] in freq_h2:
            freq_h2[hand2[0][idx]] += 1
        else:
            freq_h2[hand2[0][idx]] = 1
    if max(freq_h1.values()) > max(freq_h2.values()):
        return 1
    elif max(freq_h2.values()) > max(freq_h1.values()):
        return -1
    else:
        for h1, h2 in zip(sorted(freq_h1.values(), reverse=True), sorted(freq_h2.values(), reverse=True)):
            if h1 > h2:
                return 1
            elif h2 > h1:
                return -1
        for i, j in zip(hand1[0], hand2[0]):
            h1ord = ord(i)
            h2ord = ord(j)
            if i in ord_change.keys():
                h1ord = ord_change[i]
            if j in ord_change.keys():
                h2ord = ord_change[j]
            if h1ord == h2ord:
                continue
            elif h1ord > h2ord:
                return 1
            else:
                return -1
    return 0


def main() -> None:
    """
    Advent Of Code Day 7
    :return: None
    """
    with open('input/daySeven.txt', 'r') as file:
        hands = [(line.split()) for line in file.readlines()]
    hands.sort(key=functools.cmp_to_key(hand_values))
    print(hands)
    multiplier = 1
    sum = 0
    for hand in hands:
        sum += (int(hand[1]) * multiplier)
        multiplier += 1
    print('Part1:', sum)


if __name__ == '__main__':
    main()
