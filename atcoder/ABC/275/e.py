from functools import lru_cache
from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


@lru_cache(maxsize=None)
def mod_pow(n, m):
    if m == 0 or n == 1:
        return 1
    # NOTE: need % mod, because the number of result becomes so huge
    if m % 2 == 0:
        return mod_pow(n, m//2) * mod_pow(n, m//2) % MOD
    return n * mod_pow(n, m//2) * mod_pow(n, m//2) % MOD


N, M, K = map(int, input().split())
MOD = 998244353
mod_inverse = mod_pow(M, MOD-2)
dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1
for i in range(K):
    for j in range(N+1):
        if dp[i][j] == 0:
            continue
        # NOTE: finish this game, when a piece reach goal regardless of the number of spinning a roulette
        if j == N:
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            continue
        for k in range(1, M+1):
            nxt = j + k
            # NOTE: move back when a piece is beyond the goal
            if nxt > N:
                nxt = N - nxt % N
            dp[i+1][nxt] = (dp[i+1][nxt] + dp[i][j] * mod_inverse) % MOD
print(dp[-1][-1])
