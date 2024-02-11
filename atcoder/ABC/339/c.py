N = int(input())
A = list(map(int, input().split()))
mi = pow(10, 18)
cur = 0
for a in A:
    cur += a
    mi = min(mi, cur)
print(cur + (0 if mi >= 0 else abs(mi)))
