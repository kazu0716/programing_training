N, C = map(int, input().split())
xv = [tuple(map(int, input().split())) for _ in range(N)]
r_accum = [0]
for _, v in xv:
    r_accum.append(r_accum[-1] + v)
r_max = [0]
for i in range(1, N + 1):
    r_accum[i] -= xv[i - 1][0]
    r_max.append(max(r_max[-1], r_accum[i]))
l_accum = [0]
for _, v in xv[::-1]:
    l_accum.append(l_accum[-1] + v)
l_max = [0]
for i in range(1, N + 1):
    l_accum[i] -= C - xv[-i][0]
    l_max.append(max(l_max[-1], l_accum[i]))
ans = 0
for i in range(1, N + 1):
    ans = max(ans, r_max[i], r_accum[i] - xv[i - 1][0] + l_max[N - i])
for i in range(1, N + 1):
    ans = max(ans, l_max[i], l_accum[i] - (C - xv[-i][0]) + r_max[N - i])
print(ans)
