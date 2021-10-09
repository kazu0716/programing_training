N, P = map(int, input().split())
ans = 0

for a in list(map(int, input().split())):
    if a < P:
        ans += 1

print(ans)
