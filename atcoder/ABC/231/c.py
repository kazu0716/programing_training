from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
for _ in range(Q):
    x = int(input())
    ans.append(N-bisect_left(A, x))

print(*ans, sep="\n")
