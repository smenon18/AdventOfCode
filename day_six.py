

def main():
    """
    Day Six Problem for Advent Of Code 2022
    :return: None
    """
    file = open('./input/daySix.txt', "r")
    signal = file.read()
    file.close()
    for i in range(len(signal)-4):
        if len(set(signal[i:i + 4])) == 4:
            print("Part A:")
            print(i + 4)
            print(set(signal[i:i + 4]))
            break
    for i in range(len(signal)-14):
        if len(set(signal[i:i+14])) == 14:
            print("Part B:")
            print(i+14)
            print(set(signal[i:i + 14]))
            break


if __name__ == "__main__":
    main()
