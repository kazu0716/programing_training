L, R = map(int, input().split())

ans = float("inf")

if R - L > 2019:
    ans = 0
else:
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j) % 2019)

print(ans)
