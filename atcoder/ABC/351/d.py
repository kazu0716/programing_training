from collections import deque, defaultdict
from typing import Dict, Set


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def cast_pos_idx(h, w):
    return h * W + w


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] != ".":
            continue
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nw, nh = w + dw, h + dh
            if not (0 <= nw < W and 0 <= nh < H):
                continue
            if S[nh][nw] == "#":
                S[h][w] = "+"
visited = [[False] * W for _ in range(H)]
uf = UnionFind(H * W)
for h in range(H):
    for w in range(W):
        if S[h][w] != "." or visited[h][w]:
            continue
        visited[h][w] = True
        deq = deque([(w, h)])
        while deq:
            cw, ch = deq.popleft()
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nh, nw = ch + dh, cw + dw
                if 0 <= nw < W and 0 <= nh < H and S[nh][nw] == "." and not visited[nh][nw]:
                    visited[nh][nw] = True
                    deq.append((nw, nh))
                    uf.union(cast_pos_idx(ch, cw), cast_pos_idx(nh, nw))
tree_size = defaultdict(int)
for p in uf.roots():
    tree_size[p] = uf.size(p)
# NOTE: manage only adding count of adjacent magnets each a part of tree
counted: Dict[int, Set[int]] = defaultdict(set)
for h in range(H):
    for w in range(W):
        if S[h][w] != "+":
            continue
        idx = cast_pos_idx(h, w)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if not (0 <= nw < W and 0 <= nh < H):
                continue
            p = uf.find(cast_pos_idx(nh, nw))
            if S[nh][nw] == "." and idx not in counted[p]:
                tree_size[p] += 1
                counted[p].add(idx)
print(max(tree_size.values()))
