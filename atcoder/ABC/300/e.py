from functools import reduce


def mul_mod(x, y):
    return x * y % MOD


def simple_factorize():
    for i in range(60):
        if pow(2, i) > N:
            break
        for j in range(38):
            if pow(2, i) * pow(3, j) > N:
                break
            for k in range(26):
                s = pow(2, i) * pow(3, j) * pow(5, k)
                if s > N:
                    break
                if s == N:
                    return i, j, k
    return 0, 0, 0


N = int(input())
MOD = 998244353

a, b, c = simple_factorize()
if a == b == c == 0:
    print(0)
    exit()

ans = 0
for j in range(b + 1):
    for i in range((a - j) // 2 + 1):
        if a + b + c - i - j >= 1:
            p = reduce(mul_mod, range(1, a + b + c - i - j + 1))
            p *= pow(pow(5, a + b + c - i - j, MOD), MOD - 2, MOD)
        if a - 2 * i - j >= 1:
            p *= pow(reduce(mul_mod, range(1, a - 2 * i - j + 1)), MOD - 2, MOD)
        if b - j >= 1:
            p *= pow(reduce(mul_mod, range(1, b - j + 1)), MOD - 2, MOD)
        if i >= 1:
            p *= pow(reduce(mul_mod, range(1, i + 1)), MOD - 2, MOD)
        if j >= 1:
            p *= pow(reduce(mul_mod, range(1, j + 1)), MOD - 2, MOD)
        if c >= 1:
            p *= pow(reduce(mul_mod, range(1, c + 1)), MOD - 2, MOD)
        ans += p
        ans %= MOD
print(ans)
