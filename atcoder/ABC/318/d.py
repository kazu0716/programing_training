from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def dfs(visited, cost):
    global ans

    ans = max(ans, cost)
    if all(visited):
        return
    i = visited.index(False)
    visited[i] = True
    for j in range(i + 1, N):
        if not visited[j]:
            visited[j] = True
            dfs(visited, cost + D[i][j])
            visited[j] = False
    visited[i] = False


N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j, d in enumerate(map(int, input().split())):
        D[i][j + i + 1] = D[j + i + 1][i] = d
ans = 0
# NOTE: When N is even, all nodes are used
if N % 2 == 0:
    visited = [False] * N
    dfs(visited, 0)
    exit(print(ans))
# NOTE: When N is odd, one node is not used
for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(visited, 0)
print(ans)
