from collections import defaultdict


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def all_sizes(self):
        sizes = []

        for i in range(self.n):
            size = self.parents[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N = int(input())
A = list(map(int, input().split()))

uf = UnionFind(2*pow(10, 5)+1)

if N % 2 == 0:
    first = A[:N // 2]
    letter = A[N // 2:][::-1]
else:
    first = A[:N // 2]
    letter = A[N // 2 + 1:][::-1]

for x, y in zip(first, letter):
    uf.union(x, y)

ans = 0
for size in uf.all_sizes():
    ans += size - 1

print(ans)
