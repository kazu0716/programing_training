from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))

set_param("max_unroll_recursion=-1")


def dfs(cur):
    global ans

    if cur >= N:
        if set() not in team:
            ans += 1
        return

    if frozenset(map(frozenset, team)) in visited:
        return
    visited.add(frozenset(map(frozenset, team)))

    for i in range(T):
        if hates[cur] & team[i]:
            continue
        team[i].add(cur)
        dfs(cur + 1)
        team[i].discard(cur)


N, T, M = map(int, input().split())
hates = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    hates[A - 1].add(B - 1)
    hates[B - 1].add(A - 1)
team = [set() for _ in range(T)]
visited = set()
ans = 0
dfs(0)
print(ans)
