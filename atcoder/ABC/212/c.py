from bisect import bisect_left

N, M = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))

B.sort()

ans = pow(10, 10)

for i in range(N):
    a = A[i]
    idx = bisect_left(B, a)
    if idx == 0:
        b = B[idx]
        ans = min(ans, abs(a-b))
    elif idx == M:
        b = B[idx-1]
        ans = min(ans, abs(a-b))
    else:
        b1, b2 = B[idx-1], B[idx]
        ans = min(ans, abs(a-b1), abs(a-b2))

print(ans)
