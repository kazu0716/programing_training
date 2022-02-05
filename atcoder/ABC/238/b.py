N = int(input())
A = list(map(int, input().split()))
cur, rad = 0, set([0, 360])
for a in A:
    cur = (cur+a) % 360
    rad.add(cur)
rad = sorted(list(rad))
ans = 0
for i in range(len(rad)-1):
    ans = max(ans, abs(rad[i]-rad[i+1]))
print(ans)
