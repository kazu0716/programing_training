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


N, M = map(int, input().split())
uf = UnionFind(N)
cnt = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    if not uf.same(u - 1, v - 1):
        uf.union(u - 1, v - 1)
    cnt[u - 1] += 1
    cnt[v - 1] += 1
node_edge_cnt = defaultdict(lambda: [0, 0])
for i in range(N):
    p = uf.find(i)
    node_edge_cnt[p][0] += 1
    node_edge_cnt[p][1] += cnt[i]
for node_cnt, edge_cnt in node_edge_cnt.values():
    if node_cnt != edge_cnt // 2:
        print("No")
        exit()
print("Yes")
