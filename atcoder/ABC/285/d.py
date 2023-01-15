from collections import defaultdict


class UnionFind():
    def __init__(self):
        self.parents = defaultdict(lambda: -1)

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


def str_to_int(s):
    num = 0
    for i, ss in enumerate(s[::-1]):
        num += (ord(ss) - ord("a") + 1) * pow(26, i)
    return num


N = int(input())
uf = UnionFind()
for _ in range(N):
    S, T = map(str_to_int, input().split())
    if uf.same(S, T):
        print("No")
        exit()
    uf.union(S, T)
print("Yes")
