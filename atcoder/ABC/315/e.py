from collections import deque


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


N = int(input())
uf = UnionFind(N)
graph = [[] for _ in range(N)]
in_cnt = [0] * N
for i in range(N):
    for p in list(map(int, input().split()))[1:]:
        uf.union(i, p - 1)
        graph[p - 1].append(i)
        in_cnt[i] += 1
deq = deque([i for i in range(N) if in_cnt[i] == 0])
ans = []
while deq:
    cur = deq.popleft()
    ans.append(cur + 1)
    for nxt in graph[cur]:
        in_cnt[nxt] -= 1
        if in_cnt[nxt] == 0:
            deq.append(nxt)
print(*[a for a in ans if uf.same(a - 1, 0) and a > 1])
