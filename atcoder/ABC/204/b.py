N = int(input())

ans = 0

for a in map(int, input().split()):
    if a > 10:
        ans += a-10

print(ans)
