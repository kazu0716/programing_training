from bisect import bisect_left, bisect_right
from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().rstrip().split()))
A.sort()
ans = 0

for i in range(N-1):
    right = bisect_right(A, A[i])
    left = bisect_left(A, A[i])

    if right > i and left >= i:
        cnt = right - left
    elif right > i and left < i:
        cnt = right - i
    else:
        cnt = 0
    ans += N - i - cnt

print(ans)
