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
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


N, M = map(int, input().split())
uf, cnt = UnionFind(N), [0] * N
has_cycle = False
edges = [tuple(map(int, input().split())) for _ in range(M)]
for u, v in edges:
    cnt[u - 1] += 1
    cnt[v - 1] += 1
    if cnt[u - 1] > 2 or cnt[v - 1] > 2:
        print("No")
        exit()
    if uf.same(u - 1, v - 1):
        print("No")
        exit()
    uf.union(u - 1, v - 1)
if len(uf.roots()) > 1:
    print("No")
    exit()
print("Yes")
