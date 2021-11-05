N, K = map(int, input().split())
MOD = pow(10, 9)+7


def comb(n, r):
    if r < 0:
        return 0
    ret, fact = 1, 1
    for i in range(r):
        ret = (ret*(n-i)) % MOD
        fact = (fact*(i+1)) % MOD
    return ret*pow(fact, MOD-2, MOD) % MOD


ans = []
for i in range(1, K+1):
    r, b = (N-K)-(i-1), K-i
    ans.append((comb(i+b-1, b)*comb(i+r, r)) % MOD)

print(*ans, sep="\n")
