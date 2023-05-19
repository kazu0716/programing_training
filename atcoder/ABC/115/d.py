from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def get_patty_num(n, x):
    if n == 0:
        return 1
    if x == 1:
        return 0
    if 1 < x < A[n - 1] + 2:
        return get_patty_num(n - 1, x - 1)
    if x == A[n - 1] + 2:
        return P[n - 1] + 1
    if A[n - 1] + 2 < x < 2 * A[n - 1] + 3:
        return P[n - 1] + 1 + get_patty_num(n - 1, x - A[n - 1] - 2)
    if x == 2 * A[n - 1] + 3:
        return 2 * P[n - 1] + 1


N, X = map(int, input().split())
A, P = [1], [1]
for i in range(N):
    A.append(2 * A[-1] + 3)
    P.append(2 * P[-1] + 1)
print(get_patty_num(N, X))
