N, Q = map(int, input().split())
cnt = [0] * N
ans = []
for _ in range(Q):
    i, x = map(int, input().split())
    if i == 1:
        cnt[x - 1] += 1
    elif i == 2:
        cnt[x - 1] += 2
    else:
        ans.append("Yes" if cnt[x - 1] >= 2 else "No")
print(*ans, sep="\n")
