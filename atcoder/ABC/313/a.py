N = int(input())
P = tuple(map(int, input().split()))
ans = 0
for i in range(1, N):
    ans = max(ans, P[i] - P[0] + 1)
print(ans)
