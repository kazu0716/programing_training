H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
for h in range(H):
    for w in range(W - 1):
        X[h][w + 1] += X[h][w]
for w in range(W):
    for h in range(H - 1):
        X[h + 1][w] += X[h][w]
Q = int(input())
ans = []
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    h1, w1 = A - 2, B - 2
    h2, w2 = A - 2, D - 1
    h3, w3 = C - 1, B - 2
    h4, w4 = C - 1, D - 1
    cnt = X[h4][w4]
    for h, w, is_add in ((h1, w1, True), (h2, w2, False), (h3, w3, False)):
        if 0 <= h < H and 0 <= w < W:
            cnt = cnt + (X[h][w] if is_add else -X[h][w])
    ans.append(cnt)
print(*ans, sep="\n")
