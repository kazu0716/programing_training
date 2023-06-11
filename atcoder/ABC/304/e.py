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

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)
good_graph = True
K = int(input())
parent_set = set()
for _ in range(K):
    x, y = map(int, input().split())
    if uf.same(x - 1, y - 1):
        good_graph = False
        break
    p_x, p_y = uf.find(x - 1), uf.find(y - 1)
    if p_x > p_y:
        p_x, p_y = p_y, p_x
    parent_set.add((p_x, p_y))
Q = int(input())
ans = [] if good_graph else ["No"] * Q
for _ in range(Q):
    p, q = map(int, input().split())
    if not good_graph:
        continue
    p_p, p_q = uf.find(p - 1), uf.find(q - 1)
    if p_p > p_q:
        p_p, p_q = p_q, p_p
    ans.append("Yes" if (p_p, p_q) not in parent_set else "No")
print(*ans, sep="\n")
