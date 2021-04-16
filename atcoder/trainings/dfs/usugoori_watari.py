import sys

sys.setrecursionlimit(10**7)

m = int(input())
n = int(input())
dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))

f = [[] for _ in range(n+2)]
vis = [[False]*(m+2) for _ in range(n+2)]
ans = 0

f[0] = [0]*(m+2)
for i in range(1, n+1):
    f[i] = [0]+list(map(int, input().split()))+[0]
f[n+1] = [0]*(m+2)


def dfs(x, y, d):
    global ans

    if f[y][x] == 0:
        return
    d += 1
    ans = max(ans, d)
    vis[y][x] = True

    for dx, dy in dxdy:
        if not vis[y + dy][x + dx]:
            dfs(x + dx, y + dy, d)

    vis[y][x] = False


for x in range(1, m+1):
    for y in range(1, n+1):
        if not vis[y][x]:
            dfs(x, y, 0)

print(ans)
