from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def get_jewels(n, is_red) -> int:
    if n <= 1:
        return 0 if is_red else 1
    return get_jewels(n-1, True) + get_jewels(n, False) * X if is_red else get_jewels(n-1, True) + get_jewels(n-1, False) * Y


N, X, Y = map(int, input().split())
print(get_jewels(N, True))
