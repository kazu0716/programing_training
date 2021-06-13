import sys
from bisect import bisect_right

sys.setrecursionlimit(pow(10, 9))

N, Q = map(int, input().split())
A = list(map(int, input().split()))

def solve(k, idx1):
    idx2 = bisect_right(A, k)
    if idx1 < idx2:
        solve(k+(idx2-idx1), idx2)
    else:
        print(k)


for _ in range(Q):
    k = int(input())
    solve(k, 0)
