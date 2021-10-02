N = int(input())
S = []

dp = [[set([]) for _ in range(3)] for _ in range(N)]

for s in input():
    if s == "R":
        S.append(0)
    elif s == "G":
        S.append(1)
    else:
        S.append(2)

for i in range(N-1, -1, -1):
    c = S[i]
    if i == N-1:
        dp[i][c].add(i)
        continue
    for j in range(3):
        dp[i][j] = dp[i+1][j].copy()
        if j == c:
            dp[i][j].add(i)


ans = 0
colors = set([0, 1, 2])

for i in range(N-2):
    c1 = S[i]
    for c2 in (colors - set([c1])):
        c3 = (colors - set([c1, c2])).pop()
        for j in dp[i][c2]:
            k = 2 * j - i
            if k not in dp[j][c3]:
                ans += len(dp[j][c3])
            else:
                ans += len(dp[j][c3]) - 1

print(ans)
