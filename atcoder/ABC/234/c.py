K = int(input())

p = []
for n in range(60, -1, -1):
    k = pow(2, n)
    if K - k < 0:
        continue
    p.append(n)
    K -= k

ans = [2] + [0]*p[0]
for i in range(1, len(p)):
    idx = -(p[i]+1)
    ans[idx] = 2

print(*ans, sep="")
