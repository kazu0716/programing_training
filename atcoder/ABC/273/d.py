from bisect import bisect_left
from collections import defaultdict
from sys import stdin

input = stdin.readline

H, W, rs, cs = map(int, input().split())
h_blocks, w_blocks = defaultdict(list), defaultdict(list)
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    h_blocks[r].append(c)
    w_blocks[c].append(r)
for h in h_blocks:
    h_blocks[h].append(0)
    h_blocks[h].append(W+1)
    h_blocks[h].sort()
for w in w_blocks:
    w_blocks[w].append(0)
    w_blocks[w].append(H+1)
    w_blocks[w].sort()
Q = int(input())
ans = []
for _ in range(Q):
    d, l = input().split()
    if d == "U":
        nxt = w_blocks[cs][bisect_left(w_blocks[cs], rs) - 1] + 1 if cs in w_blocks else 1
        rs = max(rs - int(l), nxt)
    elif d == "D":
        nxt = w_blocks[cs][bisect_left(w_blocks[cs], rs)] - 1 if cs in w_blocks else H
        rs = min(rs + int(l), nxt)
    elif d == "L":
        nxt = h_blocks[rs][bisect_left(h_blocks[rs], cs) - 1] + 1 if rs in h_blocks else 1
        cs = max(cs - int(l), nxt)
    else:
        nxt = h_blocks[rs][bisect_left(h_blocks[rs], cs)] - 1 if rs in h_blocks else W
        cs = min(cs + int(l), nxt)
    ans.append(f"{rs} {cs}")
print(*ans, sep="\n")
