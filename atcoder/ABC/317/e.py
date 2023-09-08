from collections import deque


def go_straight(i, j, di, dj):
    i, j = i + di, j + dj
    while 0 <= i < H and 0 <= j < W and (A[i][j] == "." or A[i][j] == "!"):
        A[i][j] = "!"
        i, j = i + di, j + dj


H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
INF = pow(10, 9)
commands = {"^": "U", "v": "D", "<": "L", ">": "R"}
line_sight = []
root, target = [0, 0, 0], [0, 0]
for i in range(H):
    for j in range(W):
        if A[i][j] in commands:
            line_sight.append((i, j, commands[A[i][j]]))
        elif A[i][j] == "S":
            root[0], root[1] = i, j
        elif A[i][j] == "G":
            target[0], target[1] = i, j
for i, j, command in line_sight:
    if command == "U":
        go_straight(i, j, -1, 0)
    elif command == "D":
        go_straight(i, j, 1, 0)
    elif command == "L":
        go_straight(i, j, 0, -1)
    else:
        go_straight(i, j, 0, 1)
deq = deque([root])
dist = [[INF] * W for _ in range(H)]
dist[root[0]][root[1]] = 0
while deq:
    i, j, d = deq.popleft()
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nxt_i, nxt_j = i + di, j + dj
        if not (0 <= nxt_i < H and 0 <= nxt_j < W) or (A[nxt_i][nxt_j] != "." and A[nxt_i][nxt_j] != "G"):
            continue
        if dist[nxt_i][nxt_j] > d + 1:
            dist[nxt_i][nxt_j] = d + 1
            if A[nxt_i][nxt_j] != "G":
                deq.append((nxt_i, nxt_j, d + 1))
print(dist[target[0]][target[1]] if dist[target[0]][target[1]] < INF else -1)
