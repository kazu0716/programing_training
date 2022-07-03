N, X = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
s, ans = sum(AB[0]), AB[0][0] + AB[0][1] * X
for i in range(1, min(N, X)):
    s += sum(AB[i])
    ans = min(ans, s+AB[i][1]*(X-i-1))
print(ans)
