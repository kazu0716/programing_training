from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def dfs(x, y, i, cmd):
    for dx, dy in commands[commands.index(cmd) :] + commands[: commands.index(cmd)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and pos[nx][ny] == "T":
            for i in range(N):
                print(*pos[i])
            exit()
        if 0 <= nx < N and 0 <= ny < N and pos[ny][nx] == "-1":
            pos[ny][nx] = str(i + 1)
            dfs(nx, ny, i + 1, (dx, dy))


N = int(input())
pos = [["-1"] * N for _ in range(N)]
pos[N // 2][N // 2] = "T"
commands = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pos[0][0] = "1"
dfs(0, 0, 1, (1, 0))
