from itertools import cycle
from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def cycle_traversal(cur):
    for nxt in cycle_edge[cur]:
        if not cycle_uf.same(cur, nxt):
            cycle_uf.union(cur, nxt)
            cycle_traversal(nxt)


def traversal(cur):
    for nxt in edge[cur]:
        if not cycle_uf.same(nxt, cycle_parent) and not uf.same(cur, nxt):
            uf.union(cur, nxt)
            traversal(nxt)


N = int(input())
cycle_edge, edge = [set() for _ in range(N)], [[] for _ in range(N)]
# NOTE: create two type edge for cycle traversal and traversal after that
for _ in range(N):
    u, v = map(int, input().split())
    cycle_edge[u-1].add(v-1)
    cycle_edge[v-1].add(u-1)
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
# NOTE: remove branches from graph
dep = [i for i in range(N) if len(cycle_edge[i]) <= 1]
for d in dep:
    cur = d
    while len(cycle_edge[cur]) < 2:
        nxt = cycle_edge[cur].pop()
        cycle_edge[nxt].remove(cur)
        cur = nxt
# NOTE: unite cycle nodes
cycle_parent, cycle_uf = -1, UnionFind(N)
for i in range(N):
    if cycle_edge[i]:
        cycle_traversal(i)
        cycle_parent = cycle_uf.find(i)
        break
# NOTE: unite branch nodes to edge of cycle
uf = UnionFind(N)
for d in [i for i in range(N) if cycle_uf.same(cycle_parent, i)]:
    traversal(d)

Q = int(input())
ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    ans.append("Yes" if uf.same(x-1, y-1) else "No")
print(*ans, sep="\n")
