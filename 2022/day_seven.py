

folders = {}


def get_folder_size(name) -> int:
    folder_contents = folders[name]
    fldr_size = 0
    for size, item in folder_contents:
        if size == 'dir':
            if not name.endswith('/'):
                item = '/' + item
            fldr_size += get_folder_size(name + item)
        else:
            fldr_size += size
    return fldr_size


def main() -> None:
    """
    Day Seven Problem for Advent Of Code 2022
    :return: None
    """
    file = open('input/daySeven.txt', 'r')
    lines = file.readlines()
    working_directory = '~'  # home dir is placeholder should not actually be used
    while lines:
        line = lines.pop(0)  # get current line
        # assert(line[0] == '$')
        command = line[1:].strip()  # take out $
        if command == 'ls':
            folder_contents = []
            while lines:
                if lines[0][0] == '$':  # stop adding contents if $ is hit
                    break
                item = lines.pop(0).strip()
                size, item = item.split()
                if size != 'dir':
                    size = int(size)
                folder_contents.append((size, item))
            folders[working_directory] = folder_contents
        elif command.startswith('cd '):
            ch_dir = command[3:]  # get dir we are changing to
            if ch_dir == '/':
                working_directory = '/'
            elif ch_dir == '..':
                working_directory = working_directory[:working_directory.rindex('/')]
            else:
                if not working_directory.endswith('/'):
                    working_directory += '/'
                working_directory += ch_dir
    file.close()
    ans_a = 0
    for name in folders.keys():
        size = get_folder_size(name)
        if size <= 100000:
            ans_a += size
    print("Part A:")
    print(ans_a)
    total_space = 70000000
    needed_space = 30000000
    used = get_folder_size('/')
    unused = total_space - used
    to_free = needed_space - unused
    print("Part B:")
    print(min(get_folder_size(name) for name in folders.keys() if get_folder_size(name) >= to_free))


if __name__ == '__main__':
    main()
