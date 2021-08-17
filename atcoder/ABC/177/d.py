from collections import defaultdict

N, M = map(int, input().split())


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

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


uf = UnionFind(N)
groups = [[] for _ in range(N)]
ans = 0

for _ in range(M):
    A, B = map(int, input().split())
    uf.union(A-1, B-1)

friends = dict(uf.all_group_members())

for key in friends:
    for i in range(len(friends[key])):
        groups[i].append(friends[key][i])

for group in groups:
    if group:
        ans += 1

print(ans)
