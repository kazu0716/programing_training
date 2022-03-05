from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param('max_unroll_recursion=-1')


def solve(t, k):
    if t == 0:
        return S[k]
    elif k == 0:
        return chr((ord(S[0]) - 65 + t) % 3 + 65)
    else:
        return chr((ord(solve(t-1, k//2)) - 65 + k % 2+1) % 3 + 65)


S = input()
Q = int(input())
ans = []
for _ in range(Q):
    t, k = map(int, input().split())
    ans.append(solve(t, k-1))
print(*ans, sep="\n")
