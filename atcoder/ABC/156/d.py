def comb(r):
    ret, fact = 1, 1
    for i in range(r):
        ret = (ret*(n-i)) % MOD
        fact = (fact*(i+1)) % MOD
    return ret*pow(fact, MOD-2, MOD) % MOD


n, a, b = map(int, input().split())
MOD = pow(10, 9) + 7

s = pow(2, n, MOD) - 1
ca, cb = comb(min(a, n-a)), comb(min(b, n-b))
ans = (s - ca - cb) % MOD
print(ans)
