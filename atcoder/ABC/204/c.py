import sys

sys.setrecursionlimit(100000000)

N, M = map(int, input().split())

ans = 0
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)


def dfs(v):
    global ans

    find[v] = True
    ans += 1
    for next in graph[v]:
        if not find[next]:
            dfs(next)


if M > 0:
    for i in range(N):
        find = [False] * N
        dfs(i)
else:
    ans = N

print(ans)
