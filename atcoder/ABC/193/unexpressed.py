from math import sqrt

N = int(input())
range_ = range(2, N)
ans = []

for a in range(2, int(sqrt(N))+1):
    for b in range_:
        p = pow(a, b)
        if p > N:
            break
        ans.append(p)

s = set(ans)
print(N-len(s))
