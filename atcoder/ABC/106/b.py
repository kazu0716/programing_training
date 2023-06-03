N = int(input())
ans = 0
for i in range(1, N + 1, 2):
    j = 1
    cnt = 0
    while j * j <= i:
        if i % j == 0:
            cnt += 1 if i == j else 2
        j += 1
    if cnt == 8:
        ans += 1
print(ans)
