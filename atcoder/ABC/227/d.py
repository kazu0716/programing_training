N, K = map(int, input().split())
A = tuple(map(int, input().split()))

high, low = pow(10, 18), 0
while high - low > 1:
    mid, s = (high + low) // 2, 0
    for i in range(N):
        s += min(mid, A[i])
    if mid*K > s:
        high = mid
    else:
        low = mid

print(low)
