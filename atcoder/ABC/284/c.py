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

    def connected_component_size(self):
        return len([p for p in self.parents if p < 0])


N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)
print(uf.connected_component_size())
