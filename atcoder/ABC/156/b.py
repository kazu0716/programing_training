import sys

sys.setrecursionlimit(pow(10, 9))

N, K = map(int, input().split())


def solve(n, k):
    if n//k:
        return solve(n//k, k)+str(n % k)
    return str(n % k)


print(len(solve(N, K)))
