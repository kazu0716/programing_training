from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def dfs(cur):
    global length
    h, w = cur
    if S[h][w] != target[length % 5] or cur in visited:
        return
    visited.add(cur)
    length += 1
    if h == H - 1 and w == W - 1:
        exit(print("Yes"))
    for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nxt_h, nxt_w = h + dh, w + dw
        if 0 <= nxt_h < H and 0 <= nxt_w < W:
            dfs((nxt_h, nxt_w))
    if length > 0:
        length -= 1


# NOTE: python is faster than pypy3 in this code
# python: https://atcoder.jp/contests/abc308/submissions/43163105
# pypy3: https://atcoder.jp/contests/abc308/submissions/43163083
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
target = "snuke"
length = 0
visited = set()
dfs((0, 0))
print("No")
