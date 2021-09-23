s, t = input(), input()

dp = [[0]*(len(t)+1) for _ in range((len(s)+1))]

for i in range(1, (len(s)+1)):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j, l = len(s), len(t), dp[-1][-1]
ans = []

while l > 0:
    if s[i-1] == t[j-1]:
        ans.append(s[i-1])
        i -= 1
        j -= 1
        l -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print(*ans[::-1], sep="")
