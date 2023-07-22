N = int(input())
A = [0] + list(map(int, input().split()))
cur = 1
for _ in range(N):
    cur = A[cur]
ans = []
while A[cur] != -1:
    ans.append(cur)
    A[cur], cur = -1, A[cur]
print(len(ans))
print(*ans)
