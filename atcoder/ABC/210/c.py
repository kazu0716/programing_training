N, K = map(int, input().split())
C = list(map(int, input().split()))

colors = {}
cnt, ans = 0, 0

for i in range(N):
    c = C[i]
    if c in colors:
        colors[c] += 1
    else:
        colors[c] = 1
        cnt += 1

    if i >= K:
        idx = C[i-K]
        colors[idx] -= 1
        if colors[idx] <= 0:
            cnt -= 1
            colors.pop(idx)

    ans = max(ans, cnt)

print(ans)
