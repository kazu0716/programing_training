N = int(input())
M = N

primes = {}
num = []

i = 2
while i*i <= M:
    if N % i == 0:
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        primes[i] = cnt
    i += 1

if N != 1:
    primes[N] = 1

for p in primes:
    for q in range(1, primes[p]+1):
        num.append(pow(p, q))

num.sort()

ans = 0
for i in range(len(num)):
    n = num[i]
    if M % n == 0:
        M //= n
        ans += 1

print(ans)
