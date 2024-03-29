from collections import deque
from typing import Union


def get_flow(state: tuple):
    return state[4] + state[0] * state[3]


def calc_mins(v_from: str, v_to: str, valves: dict) -> Union[int, None]:
    if v_from == v_to:
        return 0
    visited = set()
    visited.add(v_from)
    to_visit = deque()
    for next_tunnel in valves[v_from]['tunnels_to']:
        visited.add(next_tunnel)
        to_visit.append((next_tunnel, 1))
    while len(to_visit) > 0:
        curr, mins = to_visit.popleft()
        if curr == v_to:
            return mins
        for next_tunnel in valves[curr]['tunnels_to']:
            if next_tunnel not in visited:
                visited.add(next_tunnel)
                to_visit.append((next_tunnel, mins + 1))
    print('You are stuck')
    return None


def get_distances(valves):
    flowing_valves = [v['name'] for v in valves.values() if v['flow_rate'] > 0]
    dist_to_others = {}
    for v in valves.keys():
        dist_to_others[v] = {}
        for other in flowing_valves:
            if other is not v and other in flowing_valves:
                dist_to_others[v][other] = calc_mins(v, other, valves)
    return dist_to_others


def bfs(valve_name: str, mins_left: int, valves, part2=False) -> int:
    flowing_valves = [v['name'] for v in valves.values() if v['flow_rate'] > 0]
    dist_to_others = {}
    for v in valves.keys():
        dist_to_others[v] = {}
        for other in flowing_valves:
            if other is not v and other in flowing_valves:
                dist_to_others[v][other] = calc_mins(v, other, valves)
    max_flow = 0
    state_best = {}
    state_all = {}
    valve_states = [(mins_left, valve_name, [], 0, 0)]
    while len(valve_states) > 0:
        curr_state = valve_states.pop()
        max_flow = max(max_flow, get_flow(curr_state))
        valve = valves[curr_state[1]]
        if curr_state[0] == 0:
            continue
        if curr_state[1] not in curr_state[2] and valve['flow_rate'] > 0:
            curr_state = (curr_state[0] - 1, curr_state[1], curr_state[2][:] + [curr_state[1]],
                          curr_state[3] + valve['flow_rate'], curr_state[4] + curr_state[3])
            valve_states.append(curr_state)
            if part2:
                all_opened = tuple(sorted(curr_state[2]))
                if state_best.get(all_opened, 0) < get_flow(curr_state):
                    state_best[all_opened] = get_flow(curr_state)
                    state_all[all_opened] = curr_state
            continue
        for allowed_dest in flowing_valves:
            if allowed_dest in curr_state[2]:
                continue
            dist_to_dest = dist_to_others[curr_state[1]][allowed_dest]
            if (curr_state[0] - dist_to_dest) > 1:
                valve_states.append((curr_state[0] - dist_to_dest, allowed_dest, curr_state[2],
                                     curr_state[3], curr_state[4] + (curr_state[3] * dist_to_dest)))
    if part2:
        max_flow = 0
        for you in state_all.values():
            for elephant in state_all.values():
                state_valid = True
                for v in you[2]:
                    if v in elephant[2]:
                        state_valid = False
                        break
                if state_valid:
                    max_flow = max(max_flow, get_flow(you) + get_flow(elephant))
    return max_flow


def main() -> None:
    """
    Day sixteen of Advent of Code 2022
    :return: None
    """
    file = open('input/daySixteen.txt', 'r')
    valves = {}
    for line in file.read().split('\n'):
        l = line.split()
        name = l[1]
        flow_rate = int(l[4][5:-1])
        tunnels_to = []
        for i in range(9, len(l)):
            tunnels_to.append(l[i].strip(','))
        valves[name] = {'name': name, 'flow_rate': flow_rate, 'tunnels_to': tunnels_to, 'open': False}
    file.close()
    start = 'AA'
    print('Part A:')
    print(bfs(start, 30, valves))
    print('Part B:')
    print(bfs(start, 26, valves, True))


if __name__ == "__main__":
    main()
