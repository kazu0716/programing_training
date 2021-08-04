N = int(input())
W = list(map(int, input().split()))

ans = pow(10, 10)

for i in range(N):
    s1, s2 = sum(W[:i]), sum(W[i:])
    ans = min(ans, abs(s1 - s2))

print(ans)
