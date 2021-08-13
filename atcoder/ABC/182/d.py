from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

s = [0] + list(accumulate(A))
t = [0]
_max = [0]

ma, cnt1, cnt2 = -pow(10, 10), 0, 0
for i in range(N):
    cnt1 += A[i]
    ma = max(ma, cnt1)
    _max.append(ma)
    cnt2 += s[i]
    t.append(cnt2)

ans = 0
for i in range(N + 1):
    ans = max(ans, t[i] + _max[i])

print(ans)
