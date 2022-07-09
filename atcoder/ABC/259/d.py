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


N = int(input())
sx, sy, tx, ty = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]
uf = UnionFind(N)
s_c, t_c = -1, -1
for i in range(len(C)):
    x1, y1, r1 = C[i]
    if s_c == -1 and (sx-x1)**2 + (sy-y1)**2 == r1 ** 2:
        s_c = i
    if t_c == -1 and (tx-x1)**2 + (ty-y1)**2 == r1 ** 2:
        t_c = i
    for j in range(i+1, len(C)):
        if uf.same(i, j):
            continue
        x2, y2, r2 = C[j]
        if ((x1 != x2 or y1 != y2) and (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2) or (x1 == x2 and y1 == y2 and r1 == r2):
            uf.union(i, j)
print("Yes" if uf.same(s_c, t_c) else "No")
