N = int(input())
P = list(map(int, input().split()))
mi = P[0]
ans = 1

for i in range(1, N):
    p = P[i]
    if mi >= p:
        mi = min(mi, p)
        ans += 1

print(ans)
