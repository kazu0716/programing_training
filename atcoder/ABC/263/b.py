N = int(input())
P = [0, 0] + list(map(int, input().split()))
cur, ans = P[-1], 0
while cur > 0:
    cur = P[cur]
    ans += 1
print(ans)
