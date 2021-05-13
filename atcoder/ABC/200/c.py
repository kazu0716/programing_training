import math

N = int(input())
A = list(map(int, input().split()))

q = [0] * 200
ans = 0


def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


for a in A:
    idx = a % 200
    q[idx] += 1

for i in q:
    if i >= 2:
        ans += comb(i, 2)

print(ans)
