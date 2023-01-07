from math import sqrt


def sorted_prime_list(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit + 1, p):
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
