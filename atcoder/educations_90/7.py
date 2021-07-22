from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()
ans = []

for _ in range(Q):
    B = int(input())
    idx = bisect_left(A, B)
    if idx == 0:
        ans.append(abs(A[idx]-B))
    elif idx == N:
        ans.append(abs(A[idx-1]-B))
    else:
        ans.append(min(abs(A[idx]-B), abs(A[idx-1]-B)))

print(*ans, sep="\n")
