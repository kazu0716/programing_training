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


N, M = map(int, input().split())
uf = UnionFind(N)
ans = "Yes"
for _ in range(M):
    u, v = map(int, input().split())
    if uf.same(u - 1, v - 1):
        ans = "No"
        continue
    uf.union(u - 1, v - 1)
parent = uf.find(0)
for i in range(1, N):
    if parent != uf.find(i):
        ans = "No"
        break
print(ans)
