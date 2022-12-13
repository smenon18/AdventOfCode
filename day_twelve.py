import collections
import sys
from typing import Tuple, List, Set, Dict


def get_next_pos_list(pos: Tuple[int, int], board: List[List[int]], visited: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
    l: List[Tuple[int, int]] = []
    if pos[0] < len(board)-1:
        if board[pos[0] + 1][pos[1]] - board[pos[0]][pos[1]] <= 1 and (pos[0] + 1, pos[1]) not in visited:
            l.append((pos[0] + 1, pos[1]))
    if pos[0] > 0:
        if board[pos[0] - 1][pos[1]] - board[pos[0]][pos[1]] <= 1 and (pos[0] - 1, pos[1]) not in visited:
            l.append((pos[0] - 1, pos[1]))
    if pos[1] < len(board[pos[0]]) - 1:
        if board[pos[0]][pos[1] + 1] - board[pos[0]][pos[1]] <= 1 and (pos[0], pos[1] + 1) not in visited:
            l.append((pos[0], pos[1] + 1))
    if pos[1] > 0:
        if board[pos[0]][pos[1] - 1] - board[pos[0]][pos[1]] <= 1 and (pos[0], pos[1] - 1) not in visited:
            l.append((pos[0], pos[1] - 1))
    return l


def create_neighbor_list(board: List[List[int]]) -> Dict:
    neighbor_list = {}
    for x in range(len(board)):
        for y in range(len(board[x])):
            point = (x, y)
            neighbor_list[point] = []
            curr_val = board[x][y]
            neighbors = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            for r, c in neighbors:
                if not 0 < r < len(board) or not 0 < c < len(board[r]):
                    continue
                n_val = board[r][c]
                if n_val - curr_val <= 1:
                    neighbor_list[point].append((r, c))
    return neighbor_list


def bfs(neighbor_list: Dict, start: Tuple[int, int], end: Tuple[int, int]) -> int:
    shortest_path: Dict[Tuple[int, int], int] = {start: 0}
    queue = collections.deque(((start, 0),))
    while queue:
        pos, steps = queue.popleft()
        n_steps = steps + 1
        for neighbor in neighbor_list[pos]:
            if neighbor not in shortest_path or n_steps < shortest_path[neighbor]:
                shortest_path[neighbor] = n_steps
                if neighbor != end:
                    queue.append((neighbor, n_steps))
    try:
        return shortest_path[end]
    except KeyError:
        return sys.maxsize


def dfs(pos: Tuple[int, int], steps: int, board: List[List[int]], visited: Set[Tuple[int, int]], end: Tuple[int, int],
        neighbor_list: Dict) -> int:
    if board[pos[0]][pos[1]] == end:
        return steps
    visited.add(pos)
    next_possible = neighbor_list[pos]
    searched_steps: List[int] = []
    for n in next_possible:
        if n in visited:
            continue
        searched_steps.append(dfs(n, steps+1, board, visited, end, neighbor_list))
    visited.remove(pos)
    if len(searched_steps) == 0:
        return sys.maxsize
    return min(searched_steps)


def main() -> None:
    """
    Day Twelve problem for Advent of Code 2022
    :return: None
    """
    file = open('./input/dayTwelve.txt', 'r')
    matrix: List[List[int]] = [[ord(c) - ord('a') for c in line] for line in file.read().split('\n')]
    file.close()
    pos = (20, 0)  # hard code 'S'
    matrix[20][0] = 0  # set 'S' to 0
    end = (20, 43)  # hard code 'E'
    matrix[20][43] = 25  # set 'E' to 25
    n_list = create_neighbor_list(matrix)
    for r in matrix:
        print(r)
    print('Part A:')
    print(bfs(n_list, pos, end))
    # print(dfs(pos, 0, matrix, set(), end, n_list))
    print('Part B:')
    print(min(bfs(n_list,(x, y), end) for (x, y) in create_neighbor_list(matrix) if matrix[x][y] == 0))


if __name__ == '__main__':
    main()
