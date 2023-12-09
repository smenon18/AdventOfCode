import functools
from collections import Counter


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
    for i, j in zip(hand1[0], hand2[0]):
        if i in freq_h1:
            freq_h1[i] += 1
        else:
            freq_h1[i] = 1
        if j in freq_h2:
            freq_h2[j] += 1
        else:
            freq_h2[j] = 1
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
    multiplier = 1
    sum = 0
    for hand in hands:
        sum += (int(hand[1]) * multiplier)
        multiplier += 1
    print('Part1:', sum)
    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    strength_card = {y: x for x, y in zip(range(len(order)), order)}
    strength_hand = {
        (1, 1, 1, 1, 1): 0,
        (2, 1, 1, 1): 1,
        (2, 2, 1): 2,
        (3, 1, 1): 3,
        (3, 2): 4,
        (4, 1): 5,
        (5,): 6
    }
    hand_str_to_idx = []
    for i, hand in enumerate(hands):
        cards = hand[0]
        count = Counter(cards)
        common = count.most_common(2)
        if len(common) > 1:
            if common[0][0] == 'J':
                count[common[1][0]] += count['J']
            else:
                count[common[0][0]] += count['J']
            del count['J']
        act_hand = tuple(y for _, y in count.most_common())
        strength = tuple([strength_hand[act_hand]] + [strength_card[c] for c in cards])
        hand_str_to_idx.append([strength, i])
    hand_str_to_idx.sort()
    out = 0
    for i in range(len(hand_str_to_idx)):
        num = int(hands[hand_str_to_idx[i][1]][1]) * (i + 1)
        out += num
    print('Part 2:', out)


if __name__ == '__main__':
    main()
