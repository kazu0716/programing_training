from bisect import bisect_left

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    left, right = A[i], A[i] + M
    cnt = bisect_left(A, right) - bisect_left(A, left)
    ans = max(ans, cnt)
print(ans)
