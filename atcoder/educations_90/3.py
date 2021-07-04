import sys

sys.setrecursionlimit(pow(10, 9))

N = int(input())
graph = [[] for _ in range(N)]
dep, p = 0, -1
find = [False] * N

for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)


def dfs(v, d):
    global dep, p

    find[v] = True
    d += 1
    if d > dep:
        dep, p = d, v
    for next in graph[v]:
        if not find[next]:
            dfs(next, d)


dfs(0, 0)
find, dep = [False] * N, 0
dfs(p, 0)

print(dep)
