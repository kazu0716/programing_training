class UnionFind:
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

    def count(self):
        return len([i for i, x in enumerate(self.parents) if x < 0])


def get_nxt_list(i, j):
    nxt = []
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nxt_i, nxt_j = i + di, j + dj
        if 0 <= nxt_i < H and 0 <= nxt_j < W and grid[nxt_i][nxt_j] == "#":
            nxt.append((nxt_i, nxt_j))
    return nxt


def convert_uf_idx(i, j):
    return i * W + j


H, W = map(int, input().split())
MOD = 998244353
grid = [list(input()) for _ in range(H)]
uf = UnionFind(H * W)
reds = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            reds.append((i, j))
            continue
        for nxt_i, nxt_j in get_nxt_list(i, j):
            uf.union(convert_uf_idx(i, j), convert_uf_idx(nxt_i, nxt_j))
group_num = uf.count() - len(reds)
cnt = 0
for i, j in reds:
    p_set = set()
    for nxt_i, nxt_j in get_nxt_list(i, j):
        p_set.add(uf.find(convert_uf_idx(nxt_i, nxt_j)))
    cnt += group_num + 1 - len(p_set)
print(cnt * pow(len(reds), -1, MOD) % MOD)
