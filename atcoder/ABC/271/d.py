N, S = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[None] * (S+1) for _ in range(N+1)]
dp[0][0] = ""
for i in range(N):
    for j in range(S+1):
        if dp[i][j] is None:
            continue
        for k in range(2):
            if j + cards[i][k] <= S:
                dp[i+1][j + cards[i][k]] = dp[i][j] + ("H" if k == 0 else "T")
if dp[-1][-1] is None:
    print("No")
else:
    print("Yes")
    print(dp[-1][-1])
