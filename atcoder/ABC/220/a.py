A, B, C = map(int, input().split())

ans = 0
for c in range(0, B+1, C):
    if c >= A:
        ans = c
        break

if ans == 0:
    print(-1)
else:
    print(ans)
