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

    def size(self, x):
        return -self.parents[self.find(x)]


N = int(input())
uf = UnionFind(N)
ans = 0
edges = []

for _ in range(N-1):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

edges.sort(key=lambda x: x[2])

for u, v, w in edges:
    size1 = uf.size(u)
    size2 = uf.size(v)
    uf.union(u, v)
    ans += size1 * size2 * w

print(ans)
