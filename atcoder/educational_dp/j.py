import sys
from collections import Counter

sys.setrecursionlimit(pow(10, 9))

N = int(input())
c = Counter(list(map(int, input().split())))

dp = [[[0.0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]


def solve(i, j, k):
    s = i + j + k
    if s == 0:
        return 0.0
    if dp[i][j][k] > 0.0:
        return dp[i][j][k]
    ret = 0.0
    if i > 0:
        ret += i * solve(i-1, j, k)
    if j > 0:
        ret += j * solve(i+1, j-1, k)
    if k > 0:
        ret += k * solve(i, j+1, k-1)
    dp[i][j][k] = (ret + N) / s
    return dp[i][j][k]


print(solve(c[1], c[2], c[3]))
