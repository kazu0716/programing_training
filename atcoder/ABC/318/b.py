N = int(input())
limit = 101
cnt = [[0] * (limit) for _ in range(limit)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    cnt[A][C] += 1
    cnt[A][D] -= 1
    cnt[B][C] -= 1
    cnt[B][D] += 1
for i in range(limit):
    for j in range(limit - 1):
        cnt[i][j + 1] += cnt[i][j]
for i in range(limit - 1):
    for j in range(limit):
        cnt[i + 1][j] += cnt[i][j]
ans = 0
for i in range(limit):
    for j in range(limit):
        if cnt[i][j] > 0:
            ans += 1
print(ans)
