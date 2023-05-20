N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
while A and B:
    a, b = A[-1], B[-1]
    if abs(a - b) <= D:
        print(a + b)
        exit()
    if a < b:
        B.pop()
    else:
        A.pop()
print(-1)

# NOTE: another solution to solve D
# from bisect import bisect_right

# N, M, D = map(int, input().split())
# A = list(map(int, input().split()))
# B = sorted(list(map(int, input().split())))
# ans = -1
# INF = pow(10, 18)
# for a in A:
#     idx = bisect_right(B, a + D)
#     b = a + D if idx < M and B[idx] == a + D else B[idx - 1] if 0 <= idx - 1 else -INF
#     if a - D <= b:
#         ans = max(ans, a + b)
# print(ans)
