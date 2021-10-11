import sys

X, Y = map(int, input().split())
MOD = pow(10, 9) + 7

a, b = (2*X-Y)//3, (2*Y-X)//3
n, r = a + b, min(a, b)

if (2*X-Y) % 3 > 0 or (2*Y-X) % 3 > 0 or a < 0 or b < 0:
    print(0)
    sys.exit(0)

ret, fact = 1, 1
for i in range(r):
    ret = (ret*(n-i)) % MOD
    fact = (fact*(i+1)) % MOD

print(ret*pow(fact, MOD-2, MOD) % MOD)
