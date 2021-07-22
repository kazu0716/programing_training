from collections import deque

N, K = map(int, input().split())
S = input()

dp = deque([])
index, ans = 0, []

tmp = {}

for i in range(N):
    idx = N - (i + 1)
    char_n = ord(S[-(i+1)]) - 97
    tmp[char_n] = idx
    dp.appendleft(tmp.copy())

dp = list(dp)

while len(ans) < K:
    dic = dp[index]
    keys = sorted(dic.keys())
    n = len(ans)

    for key in keys:
        idx = dic[key]
        if N - idx < K - n:
            continue
        index = idx + 1
        ans.append(chr(key+97))
        break

print(*ans, sep="")
