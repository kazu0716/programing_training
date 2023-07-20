from collections import defaultdict

from pypyjit import set_param

set_param("max_unroll_recursion=-1")


class UnionFind():
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


N, M = map(int, input().split())
p = list(map(int, input().split()))
graph = [[] for _ in range(N)]
uf = UnionFind(N)
for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)
ans = 0
members = defaultdict(set)
for i in range(N):
    members[uf.find(i)].add(i)
for member in members.values():
    for m in member:
        if p[m] - 1 in member:
            ans += 1
print(ans)
