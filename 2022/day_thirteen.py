from typing import TypeAlias, Union


Packet: TypeAlias = Union[list, int]
PacketPair: TypeAlias = tuple[Packet, Packet]


def int_compare(x: int, y: int) -> Union[bool, None]:
    if x < y:
        return True
    elif x > y:
        return False
    return None


def list_compare(x: list[Packet], y: list[Packet]) -> Union[bool, None]:
    len_x = len(x)
    len_y = len(y)
    i = 0
    while True:
        if i == len_x and i == len_y:
            return None
        elif i == len_x:
            return True
        elif i == len_y:
            return False
        ix = x[i]
        iy = y[i]
        if isinstance(ix, int) and isinstance(iy, int):
            is_ordered = int_compare(ix, iy)
        elif isinstance(ix, int):
            is_ordered = list_compare([ix], iy)
        elif isinstance(iy, int):
            is_ordered = list_compare(ix, [iy])
        else:
            is_ordered = list_compare(ix, iy)
        if is_ordered is not None:
            return is_ordered
        i += 1


def sort(packet_list: list[Packet]) -> list[Packet]:  # standard bubble sort
    tot = len(packet_list)
    for i in range(tot):
        for j in range(tot - i - 1):
            is_ordered = list_compare(packet_list[j], packet_list[j + 1])
            if not is_ordered:
                packet_list[j], packet_list[j + 1] = packet_list[j + 1], packet_list[j]
    return packet_list


def main() -> None:
    """
    Day Thirteen of Advent of Code 2022
    :return: None
    """
    file = open('input/dayThirteen.txt', 'r')
    packet_pairs_str: list[list[str]] = [packets.split('\n') for packets in file.read().split('\n\n')]
    file.close()
    file = open('input/dayThirteen.txt', 'r')
    packet_list: list[Packet] = [eval(line) for line in file.read().split('\n') if line != '']
    file.close()
    packet_pairs: list[PacketPair] = [(eval(p[0]), eval(p[1])) for p in packet_pairs_str]
    sum_a = 0
    for i, p in enumerate(packet_pairs):
        p1, p2 = p
        val = list_compare(p1, p2)
        if val:
            sum_a += (i+1)
    print('Part A:')
    print(sum_a)
    divider_one = [[2]]
    divider_two = [[6]]
    packet_list.append(divider_one)
    packet_list.append(divider_two)
    packet_list = sort(packet_list)
    print('Part B:')
    print((packet_list.index(divider_one) + 1) * (packet_list.index(divider_two) + 1))


if __name__ == '__main__':
    main()
