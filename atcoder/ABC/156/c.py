N = int(input())
X = list(map(int, input().split()))

ans = pow(100, 100)

for p in range(1, 101):
    s = 0
    for x in X:
        s += (x-p)**2
    ans = min(ans, s)

print(ans)
