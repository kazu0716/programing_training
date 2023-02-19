from math import gcd

T = int(input())
ans = []
for _ in range(T):
    N, D, K = map(int, input().split())
    n = N // gcd(N, D)
    ans.append((K - 1) // n + (K - 1) * D % N)
print(*ans, sep="\n")
