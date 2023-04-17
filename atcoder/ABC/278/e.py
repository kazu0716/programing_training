H, W, N, h, w = map(int, input().split())
A = tuple(tuple(map(int, input().split())) for _ in range(H))

cnt = [[[0] * (N + 1) for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        cnt[i][j][A[i][j]] += 1
        for k in range(1, N + 1):
            if i - 1 >= 0:
                cnt[i][j][k] += cnt[i - 1][j][k]
            if j - 1 >= 0:
                cnt[i][j][k] += cnt[i][j - 1][k]
            if i - 1 >= 0 and j - 1 >= 0:
                cnt[i][j][k] -= cnt[i - 1][j - 1][k]

h -= 1
w -= 1
for k in range(H - h):
    ans = []
    for l in range(W - w):
        uq = 0
        for n in range(1, N + 1):
            c = cnt[-1][-1][n] - cnt[k + h][l + w][n]
            if k - 1 >= 0:
                c += cnt[k - 1][l + w][n]
            if l - 1 >= 0:
                c += cnt[k + h][l - 1][n]
            if k - 1 >= 0 and l - 1 >= 0:
                c -= cnt[k - 1][l - 1][n]
            if c > 0:
                uq += 1
        ans.append(uq)
    print(*ans)
