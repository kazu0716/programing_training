from collections import defaultdict
from re import compile

N = int(input())
A = list(map(int, input().split()))
S = input()
m_key = ["M0", "M1", "M2"]
me_key = [m + e for m in m_key for e in ("E0", "E1", "E2")]
mex_key = [me + x for me in me_key for x in ("X0", "X1", "X2")]
dp = [defaultdict(int) for _ in range(N + 1)]
for i, s in enumerate(S):
    for k in dp[i]:
        dp[i + 1][k] = dp[i][k]
    if s == "M":
        dp[i + 1][f"{s}{A[i]}"] += 1
    elif s == "E":
        for m in m_key:
            dp[i + 1][f"{m}{s}{A[i]}"] += dp[i][m]
    else:
        for me in me_key:
            dp[i + 1][f"{me}{s}{A[i]}"] += dp[i][me]
ans = 0
p = compile(r"\d+")
for k in mex_key:
    ans += dp[-1][k] * min({0, 1, 2, 3} - set(map(int, p.findall(k))))
print(ans)
