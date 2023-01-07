from math import sqrt


def sorted_prime_list(limit):
    limit += 1
    primes, is_prime = [], [True] * limit
    for i in range(2 ** 2, limit, 2):
        is_prime[i] = False
    for p in range(3, limit, 2):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit, p):
            is_prime[i] = False
    return primes


T = int(input())
N = [int(input()) for _ in range(T)]
primes = sorted_prime_list(min(max(N), 3 * pow(10, 6)))
for n in N:
    p_or_q = 2
    for prime in primes:
        if pow(n, 1 / 3) + 1 < prime:
            break
        if n % prime == 0:
            p_or_q = max(p_or_q, prime)
    ans = (p_or_q, n // p_or_q ** 2) if n % p_or_q ** 2 == 0 else (round(sqrt(n // p_or_q)), p_or_q)
    print(*ans)
