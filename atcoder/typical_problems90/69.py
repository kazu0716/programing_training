N, K = map(int, input().split())
MOD = pow(10, 9)+7
ans = 1
for i in range(min(3, N)):
    if i == 0:
        ans = ans * K % MOD
    elif i == 1:
        ans = ans * (K-1) % MOD
    else:
        ans = ans * pow(K-2, N-2, MOD) % MOD
print(ans)
