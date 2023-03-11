from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def group_count(self):
        return len([i for i, x in enumerate(self.parents) if x < 0])


N, M = map(int, input().split())
uf = UnionFind(N)
has_cycle = defaultdict(bool)
for _ in range(M):
    A, _, C, _ = input().split()
    A, C = int(A), int(C)
    if uf.same(A - 1, C - 1):
        has_cycle[uf.find(A - 1)] = True
        continue
    uf.union(A - 1, C - 1)
cnt = uf.group_count()
print(len(has_cycle), cnt - len(has_cycle))
