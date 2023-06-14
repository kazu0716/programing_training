from operator import itemgetter

_, M = map(int, input().split())
ans, r = 0, -1
for a, b in sorted([tuple(map(int, input().split())) for _ in range(M)], key=itemgetter(1)):
    if r <= a:
        r = b
        ans += 1
print(ans)
