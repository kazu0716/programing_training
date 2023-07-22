N, D = map(int, input().split())
cnt = [0] * D
for _ in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == "o":
            cnt[j] += 1
cur = ans = 0
for i in range(D):
    if cnt[i] == N:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 0
print(max(ans, cur))
