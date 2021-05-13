N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]

ans = float("INF")

for apx in APX:
    apx[2] -= apx[0]
    if apx[2] > 0:
        ans = min(ans, apx[1])

if ans == float("INF"):
    print(-1)
else:
    print(ans)
