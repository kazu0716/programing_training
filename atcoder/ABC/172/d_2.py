N = int(input())

ans = 0

for i in range(1, N+1):
    s, cnt = 0, 0
    for j in range(i, N+1, i):
        cnt += 1
        s += cnt * i
    ans += s

print(ans)
