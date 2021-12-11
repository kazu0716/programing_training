from sys import exit


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
edge = [set([]) for _ in range(N)]
cnt = [0]*N
uf = UnionFind(N)

for _ in range(M):
    A, B = map(int, input().split())
    edge[A-1].add(B-1)
    edge[B-1].add(A-1)
    cnt[A-1] += 1
    cnt[B-1] += 1
    if cnt[A-1] > 2 or cnt[B-1] > 2:
        print("No")
        exit()

for i in range(N):
    if not edge[i]:
        continue
    while edge[i]:
        nxt = edge[i].pop()
        if uf.same(i, nxt):
            print("No")
            exit()
        uf.union(i, nxt)
        edge[nxt].remove(i)

print("Yes")
