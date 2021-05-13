a, b = map(int, input().split())
c, d = map(int, input().split())

ans = - pow(10, 3)

for x in range(a, b+1):
    for y in range(c, d+1):
        ans = max(ans, x-y)

print(ans)
