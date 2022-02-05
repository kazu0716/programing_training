
N = int(input())
MOD = 998244353


def _sum(n):
    return n*(n+1)//2


l = len(str(N))-1
ans = _sum(N-pow(10, l)+1) % MOD
nine = 0
for i in range(l):
    nine += 9*pow(10, i)
    ini = pow(10, i)
    ans = (ans+_sum(nine-ini+1)) % MOD
print(ans)
