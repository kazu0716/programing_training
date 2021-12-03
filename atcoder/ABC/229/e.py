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


N, M = map(int, input().split())
edge = [[] for _ in range(N)]
uf = UnionFind(N)

for _ in range(M):
    A, B = map(int, input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)

cnt, ans = 0, [0]
for cur in range(N-1, 0, -1):
    cnt += 1
    for nxt in edge[cur]:
        if nxt <= cur:
            continue
        if uf.same(cur, nxt):
            continue
        uf.union(cur, nxt)
        cnt -= 1
    ans.append(cnt)

print(*ans[::-1], sep="\n")
