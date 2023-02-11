N = int(input())
A = list(map(int, input().split()))
_ = input()
B = set(map(int, input().split()))
X = int(input())
dp = [False] * (X + 1)
dp[0] = True
for i in range(X):
    if not dp[i]:
        continue
    for a in A:
        nxt = i + a
        if nxt > X or nxt in B:
            continue
        dp[nxt] = True
print("Yes" if dp[-1] else "No")
