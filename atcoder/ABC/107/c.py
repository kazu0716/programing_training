from bisect import bisect_left

N, K = map(int, input().split())
X = sorted(list(map(int, input().split())) + [0])
accum = [0]
for i in range(N):
    d = X[i + 1] - X[i]
    accum.append(accum[-1] + d)
zero_pos = bisect_left(X, 0)
ans = pow(10, 18)
for i in range(K + 1):
    left = zero_pos - i
    right = zero_pos + K - i
    if not (0 <= left < len(accum) and 0 <= right < len(accum)):
        continue
    dis = accum[right] - accum[left] + min(accum[right] - accum[zero_pos], accum[zero_pos] - accum[left])
    ans = min(ans, dis)
print(ans)
