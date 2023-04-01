from math import ceil, sqrt

INF = pow(10, 18)


def solve(n, m):
    if n >= m:
        return m
    if n * n < m:
        return -1

    ans = INF
    for a in range(1, ceil(sqrt(m)) + 1):
        b = ceil(m / a)
        if 1 <= a <= n and 1 <= b <= n:
            ans = min(ans, a * b)

    return ans if ans < INF else -1


N, M = map(int, input().split())
print(solve(N, M))
