N = int(input())
degrees = [0] * N
for _ in range(N - 1):
    u, v = map(int, input().split())
    degrees[u - 1] += 1
    degrees[v - 1] += 1
ans = [d for d in degrees if d >= 3]
d2_cnt = len([d for d in degrees if d == 2]) - 2 * len(ans)
if d2_cnt > 0:
    ans += [2] * (d2_cnt // 3 + 1)
print(*sorted(ans))
