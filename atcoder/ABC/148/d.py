N = int(input())
A = list(map(int, input().split()))

cnt, ans = 1, 0

for i in range(N):
    if A[i] != cnt:
        continue
    ans += 1
    cnt += 1

if ans == 0:
    print(-1)
else:
    print(N - ans)
