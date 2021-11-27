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

        if x < y:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


Q = int(input())
N = pow(2, 20)
A = [-1]*N

uf = UnionFind(N+1)
ans = []

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        p = uf.find(x % N)
        if p == N:
            p = uf.find(0)
        A[p] = x
        uf.union(p, p+1)
    else:
        ans.append(A[x % N])

print(*ans, sep="\n")
