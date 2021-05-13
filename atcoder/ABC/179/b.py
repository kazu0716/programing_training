N = int(input())

cnt, max_cnt = 0, 0

for _ in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0

if max_cnt >= 3 or cnt >= 3:
    print("Yes")
else:
    print("No")
