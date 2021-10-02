N = int(input())
S = input()

dp = [[set([]), set([]), set([])] for _ in range(N)]


def convert_int(color):
    if color == "R":
        return 0
    elif color == "G":
        return 1
    else:
        return 2


for i in range(N-1, -1, -1):
    c = convert_int(S[i])
    if i == N-1:
        dp[i][c].add(i)
        continue
    for j in range(3):
        if j == c:
            dp[i][j] = dp[i+1][j].copy()
            dp[i][j].add(i)
        else:
            dp[i][j] = dp[i+1][j].copy()

ans = 0
colors = set([0, 1, 2])

for i in range(N-2):
    c1 = convert_int(S[i])
    for c2 in (colors - set([c1])):
        c3 = (colors - set([c1, c2])).pop()
        for j in dp[i][c2]:
            k = 2 * j - i
            if k not in dp[j][c3]:
                ans += len(dp[j][c3])
            else:
                ans += len(dp[j][c3]) - 1

print(ans)
