from collections import defaultdict
from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def dfs(cur):
    visited[cur] = True
    if not edge[cur]:
        return
    s_set.remove(cur)
    for nxt in edge[cur]:
        if visited[nxt]:
            print("No")
            exit()
        dfs(nxt)


N = int(input())
edge = defaultdict(list)
in_cnt = defaultdict(int)
visited = defaultdict(bool)
s_set = set()
for _ in range(N):
    S, T = input().split()
    in_cnt[S] += 0
    in_cnt[T] += 1
    edge[S].append(T)
    s_set.add(S)
deps = [k for k, v in in_cnt.items() if v < 1]
if not deps:
    print("No")
    exit()
for dep in deps:
    dfs(dep)
if s_set:
    print("No")
    exit()
print("Yes")
