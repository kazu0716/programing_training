X = int(input())

mx = 201

dp = [0] * mx
for i in range(mx):
    dp[i] = pow(i, 5)

ans = []
for i in range(mx):
    for j in range(mx):
        if dp[i] - dp[j] == X:
            ans = [i, j]
            break
        if dp[i] + dp[j] == X:
            ans = [i, -j]
            break

print(*ans)
