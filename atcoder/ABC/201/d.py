H, W = map(int, input().split())
score = [[1 if s == "+" else -1 for s in input()] for _ in range(H)]
dp = [[0]*W for _ in range(H)]
for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if h == H-1 and w == W-1:
            continue
        is_t = (h+w) % 2 == 0
        if h+1 < H and w+1 < W:
            dp[h][w] = max(dp[h+1][w]+score[h+1][w], dp[h][w+1]+score[h][w+1]) if is_t else min(dp[h+1][w]-score[h+1][w], dp[h][w+1]-score[h][w+1])
        elif h+1 < H:
            dp[h][w] = dp[h+1][w] + (score[h+1][w] if is_t else -score[h+1][w])
        elif w+1 < W:
            dp[h][w] = dp[h][w+1] + (score[h][w+1] if is_t else -score[h][w+1])
if dp[0][0] == 0:
    print("Draw")
elif dp[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")
