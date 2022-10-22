from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def dfs(cur, dep):
    if not edge[cur]:
        return
    for nxt in edge[cur]:
        ans[nxt] = dep + 1
        dfs(nxt, dep + 1)


N = int(input())
A = list(map(int, input().split()))
edge = [[] for _ in range(2 * N + 2)]
for i, a in enumerate(A):
    edge[a].append(2 * (i + 1))
    edge[a].append(2 * (i + 1) + 1)
ans = [0] * (2 * N + 2)
dfs(1, 0)
print(*ans[1:], sep="\n")
