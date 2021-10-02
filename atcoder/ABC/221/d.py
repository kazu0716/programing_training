N = int(input())
date = []

for _ in range(N):
    A, B = map(int, input().split())
    date.append((A, 1))
    date.append((A+B, -1))
date.sort(key=lambda x: x[0])

ans = [0]*N
cnt = 0
for i in range(len(date)-1):
    cnt += date[i][1]
    if cnt == 0:
        continue
    ans[cnt-1] += date[i+1][0] - date[i][0]

print(*ans)
