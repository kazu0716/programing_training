N, L, R = map(int, input().split())
A = list(map(int, input().split()))
accum_x, accum_y = [0], [0]
for i in range(N):
    accum_x.append(min(accum_x[-1] + A[i], L * (i + 1)))
    accum_y.append(min(accum_y[-1] + A[N - 1 - i], R * (i + 1)))
ans = pow(10, 18)
for i in range(N+1):
    ans = min(ans, accum_x[i] + accum_y[N - i])
print(ans)
