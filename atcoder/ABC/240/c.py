N, X = map(int, input().split())
dd = []
for _ in range(N):
    a, b = map(int, input().split())
    dd.append((a, b))
dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(X+1):
        if not dp[i-1][j]:
            continue
        for d in dd[i-1]:
            if j+d <= X:
                dp[i][j+d] = dp[i-1][j]
if dp[N][X]:
    print("Yes")
else:
    print("No")
