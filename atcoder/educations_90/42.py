from sys import exit

K = int(input())
MOD = pow(10, 9)+7

if K % 9 != 0:
    print(0)
    exit()

dp = [0]*(K+1)
dp[0] = 1
for i in range(K+1):
    for j in range(1, 10):
        if i+j > K:
            continue
        dp[i+j] = (dp[i+j]+dp[i]) % MOD

print(dp[-1])
