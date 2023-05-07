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

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(M)][::-1]
uf = UnionFind(N + 1)
ans = [N * (N - 1) // 2]
for A, B in bridges:
    if uf.same(A, B):
        ans.append(ans[-1])
        continue
    ans.append(ans[-1] - uf.size(A) * uf.size(B))
    uf.union(A, B)
print(*ans[::-1][1:], sep="\n")
