N = int(input())
ans = 0

for i in range(1, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if i % 2 == 1 and cnt == 8:
        ans += 1
print(ans)
