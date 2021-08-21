N, M = map(int, input().split())
A = tuple(map(int, input().split()))

s = set(range(1, M+1))
p = set()

for i in range(N):
    a, j = A[i], 2
    while pow(j, 2) <= a:
        if a % j == 0:
            p.add(j)
            p.add(a//j)
        j += 1
    if a != 1:
        p.add(a)

for prime in p:
    i = 1
    while prime * i <= M:
        if prime * i in s:
            s.discard(prime * i)
        i += 1

print(len(s))
print(*s, sep="\n")
