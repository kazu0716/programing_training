from collections import defaultdict
from typing import Dict


def get_primes() -> Dict[int, int]:
    # NOTE: To start 3 is faster than starting 2, because the number of loop is about half.
    primes: Dict[int, int] = defaultdict(int)
    i, k = 3, K
    while i * i <= K:
        while k % 2 == 0:
            primes[2] += 1
            k //= 2
        while k % i == 0:
            primes[i] += 1
            k //= i
        i += 2
    if k > 1:
        primes[k] += 1
    return primes


def get_index_cnt(n: int, m: int) -> int:
    index_cnt = 0
    while n % m == 0:
        n //= m
        index_cnt += 1
    return index_cnt


K = int(input())
p, ans = get_primes(), 0
for key, value in p.items():
    cnt = 0
    while value > 0:
        cnt += 1
        value -= 1 + get_index_cnt(cnt, key)
    ans = max(ans, key * cnt)

print(ans)
