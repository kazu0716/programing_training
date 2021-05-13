X, N = map(int, input().split())
P = list(map(int, input().split()))

ans = 0

for i in range(X+1):
    a, b = X-i, X+i
    if a not in P:
        ans = a
        break
    if b not in P:
        ans = b
        break

print(ans)
