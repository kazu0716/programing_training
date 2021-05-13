import sys


def solve():
    N, P = map(int, sys.stdin.readline().strip().split())
    mod = pow(10, 9)+7
    ans = (P-1)*pow(P-2, N-1, mod)
    print(ans % mod)


if __name__ == '__main__':
    solve()
