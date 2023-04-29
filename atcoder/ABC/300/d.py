from bisect import bisect_left
from math import sqrt


def eratosthenes(limit: int):
    isPrime = [True] * max(limit + 1, 2)
    isPrime[0], isPrime[1] = False, False
    # NOTE: delete even numbers
    for i in range(2 * 2, limit + 1, 2):
        isPrime[i] = False
    # NOTE: check only odd numbers
    for p in range(3, limit + 1, 2):
        if not isPrime[p]:
            continue
        for i in range(p * p, limit + 1, p):
            isPrime[i] = False
    return [i for i, b in enumerate(isPrime) if b]


N = int(input())
primes = eratosthenes(int(sqrt(N)))
ans = 0
for i in range(len(primes)):
    if pow(primes[i], 5) >= N:
        break
    for j in range(i + 2, len(primes)):
        b = N // primes[i] ** 2 // primes[j] ** 2
        k = bisect_left(primes, b)
        if k < len(primes) and primes[k] != b:
            k -= 1
        if k <= i:
            break
        ans += (j - i - 1) if k >= j else (k - i)
print(ans)
