N = int(input())

i, cnt = 2, 0
while N > 1 and i*i <= N:
    if N % i == 0:
        cnt += 1
        N //= i
    else:
        i += 1
if N > 1:
    cnt += 1
ans = 0
while cnt > 1:
    ans += 1
    cnt = cnt // 2 + cnt % 2
print(ans)
