H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [0] * min(H, W)
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if not (C[i][j] == C[i - 1][j - 1] == C[i - 1][j + 1] == C[i + 1][j - 1] == C[i + 1][j + 1] == '#'):
            continue
        d = 1
        while i + d < H and j + d < W and C[i + d][j + d] == "#":
            d += 1
        d -= 1
        for di, dj in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            if not (0 <= i + d + di < H and 0 <= j + d + dj < W) or C[i + d + di][j + d + dj] == ".":
                ans[d - 1] += 1
                break
print(*ans)
