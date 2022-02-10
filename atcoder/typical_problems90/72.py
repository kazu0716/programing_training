from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


def search(start, pre, cur, dis, finds):
    global ans
    for dh, dw in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nxt_h, nxt_w = cur[0]+dh, cur[1]+dw
        idx, nxt = nxt_h*W+nxt_w, (nxt_h, nxt_w)
        if nxt_h < 0 or nxt_h >= H or nxt_w < 0 or nxt_w >= W:
            continue
        if grid[nxt_h][nxt_w] == "#" or pre == nxt:
            continue
        if start == nxt:
            ans = max(ans, dis+1)
            return
        if finds[idx] == "1":
            continue
        search(start, cur, nxt, dis+1, finds[:idx]+"1"+finds[idx+1:])
    return


H, W = map(int, input().split())
grid = [tuple(input()) for _ in range(H)]
bit, ans = "0"*(H*W), 0
for h in range(H):
    for w in range(W):
        idx = h*W+w
        search((h, w), (-1, -1), (h, w), 0, bit[:idx]+"1"+bit[idx+1:])
if ans == 0:
    print(-1)
else:
    print(ans)
