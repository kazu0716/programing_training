N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
P = []
cur = 1
for i in range(N):
    nxt = cur * pow(N, -1, MOD) % MOD
    cur += nxt
    P.append(nxt)
ans = 0
for a, p in zip(A, P):
    ans += a * p
    ans %= MOD
print(ans)
