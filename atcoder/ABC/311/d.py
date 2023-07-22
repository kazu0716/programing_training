from collections import deque

direction = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
rev = {"U": "D", "D": "U", "R": "L", "L": "R"}


def change_direction(i, j, cur_d):
    dir_list = []
    for d in "UDRL":
        # NOTE: not get back
        if cur_d in rev and d == rev[cur_d]:
            continue
        nxt_i, nxt_j = i + direction[d][0], j + direction[d][1]
        # NOTE: check whether the next can go or not
        if grid[nxt_i][nxt_j] == "." and (nxt_i, nxt_j, d) not in visited:
            dir_list.append(d)
    return dir_list


N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
# NOTE: use visited set per direction to enable full route search
ans = set([(1, 1)])
visited = {d: set() for d in "UDRL"}
deq = deque([])
for d in change_direction(1, 1, "INI"):
    deq.append((1, 1, d))
    visited[d].add((1, 1))
while deq:
    i, j, d = deq.popleft()
    nxt_i, nxt_j = i + direction[d][0], j + direction[d][1]
    if (nxt_i, nxt_j) in visited[d]:
        continue
    # NOTE: go straight a head on ice
    if grid[nxt_i][nxt_j] == ".":
        visited[d].add((nxt_i, nxt_j))
        ans.add((nxt_i, nxt_j))
        deq.appendleft((nxt_i, nxt_j, d))
        continue
    # NOTE: change dir when face a rock
    for nxt_d in change_direction(i, j, d):
        deq.append((i, j, nxt_d))
        visited[nxt_d].add((i, j))
print(len(ans))
