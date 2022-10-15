from bisect import bisect_left
from collections import defaultdict

H, W, rs, cs = map(int, input().split())
h_blocks, w_blocks = defaultdict(list), defaultdict(list)
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    h_blocks[r].append(c)
    w_blocks[c].append(r)
for h in h_blocks:
    h_blocks[h].sort()
for w in w_blocks:
    w_blocks[w].sort()
Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == "U" or d == "D":
        idx = bisect_left(w_blocks[cs], rs)
        if d == "U":
            block = 0 if idx == 0 else w_blocks[cs][idx-1]
            nxt = max(1, rs - l, block + 1)
        else:
            block = H + 1 if idx >= len(w_blocks[cs]) else w_blocks[cs][idx]
            nxt = min(H, rs + l, block - 1)
        rs = nxt
    else:
        idx = bisect_left(h_blocks[rs], cs)
        if d == "L":
            block = 0 if idx == 0 else h_blocks[rs][idx-1]
            nxt = max(1, cs - l, block + 1)
        else:
            block = W + 1 if idx >= len(h_blocks[rs]) else h_blocks[rs][idx]
            nxt = min(W, cs + l, block - 1)
        cs = nxt
    print(rs, cs)
