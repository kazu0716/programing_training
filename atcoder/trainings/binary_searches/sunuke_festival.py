from bisect import bisect_left, bisect_right

N = int(input())
A, B, C = list(map(int, input().split())), list(
    map(int, input().split())), list(map(int, input().split()))

ans = 0

A.sort()
C.sort()

for b in B:
    idx_a = bisect_left(A, b)
    idx_c = bisect_right(C, b)
    ans += idx_a * (N - idx_c)

print(ans)
