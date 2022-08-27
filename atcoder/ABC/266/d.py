from collections import defaultdict

N = int(input())
sunuke, tmax = defaultdict(tuple), 0
for _ in range(N):
    T, X, A = map(int, input().split())
    sunuke[T], tmax = (X, A), max(T, tmax)
dp = [[-1]*5 for _ in range(tmax+1)]
dp[0][0] = 0
for t in range(1, tmax+1):
    for i in range(5):
        dp[t][i] = max(dp[t-1][max(i-1, 0)], dp[t-1][i], dp[t-1][min(i+1, 4)])
    if t in sunuke and dp[t][sunuke[t][0]] >= 0:
        dp[t][sunuke[t][0]] += sunuke[t][1]
print(max(dp[-1]))
