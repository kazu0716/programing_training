from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = sorted(A)

mi, ma = B[0], B[-1]
s = 0
dp = defaultdict(int)
ans = []


def comb(n):
    if n > 2:
        return n*(n-1)//2
    elif n == 2:
        return 1
    else:
        return 0


pre, cnt = -1, 0
for i in range(N):
    b = B[i]
    if pre != b and pre != -1:
        s += comb(cnt)
        dp[pre] = cnt
        cnt = 0
    pre = b
    cnt += 1

s += comb(cnt)
dp[pre] = cnt

for i in range(N):
    a = A[i]
    n1, n2 = dp[a], dp[a]-1
    c1, c2 = comb(n1), comb(n2)
    dif = c1-c2
    ans.append(s-dif)

print(*ans, sep="\n")
