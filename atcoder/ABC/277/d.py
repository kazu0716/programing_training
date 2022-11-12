from collections import Counter, defaultdict
from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


class UnionFind():
    def __init__(self):
        self.parents = defaultdict(lambda: -1)

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


def dfs(cur):
    nxt = (cur + 1) % M
    if uf.find(cur) != uf.find(nxt) and nxt in cnt:
        uf.union(cur, nxt)
        dfs(nxt)


N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = dict(Counter(A))
uf = UnionFind()
for key in cnt:
    dfs(key)
score = defaultdict(int)
for key in cnt:
    p = uf.find(key)
    score[p] += cnt[key] * key
print(sum(A) - max(score.values()))
