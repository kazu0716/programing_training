from math import sqrt


def get_sieve_of_eratosthenes(n):
    prime = []
    limit = sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


N = int(input())
primes = get_sieve_of_eratosthenes(int(pow(N, 1/3))+10)
ans = 0
for i in range(len(primes)-1):
    if pow(primes[i], 4) > N:
        break
    for j in range(i+1, len(primes)):
        if primes[i] * pow(primes[j], 3) <= N:
            ans += 1
            continue
        break
print(ans)
