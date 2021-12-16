from functools import reduce
from math import gcd
from sys import exit

N = int(input())
A = list(map(int, input().split()))
A.sort()

if reduce(gcd, A) > 1:
    print("not coprime")
    exit()

i, dp = 2, [1]*(A[-1]+1)
while i <= A[-1]:
    for j in range(2*i, A[-1]+1, i):
        if dp[j] != 1:
            continue
        dp[j] = i
    i += 1

primes = set([])
for a in A:
    tmp = set([])
    while dp[a] > 1:
        tmp.add(dp[a])
        a = a // dp[a]
    if a > 1:
        tmp.add(a)
    for t in tmp:
        if t in primes:
            print("setwise coprime")
            exit()
        primes.add(t)

print("pairwise coprime")
