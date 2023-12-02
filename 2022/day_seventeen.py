

def main() -> None:
    """
    Day Seventeen of Advent of Code 2022
    :return: None
    """
    file = open('input/daySeventeen.txt', 'r')
    push_seq = list(file.read())
    file.close()
    width = 7  # width is seven spawn 3 from left
    h = 3  # curr height is lowest block + 3 / floor + 3 for no blocks
    print(len(push_seq))
    j = 0  # jet counter
    for i in range(2022):
        print(i)


if __name__ == '__main__':
    main()
