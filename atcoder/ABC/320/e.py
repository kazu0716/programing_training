from heapq import heapify, heappop, heappush
from typing import List, Tuple

N, M = map(int, input().split())
line = [i for i in range(N)]
heapify(line)
amount = [0] * N
returns: List[Tuple[int, int]] = []
for _ in range(M):
    T, W, S = map(int, input().split())
    # NOTE: return people
    while returns and returns[0][0] <= T:
        _, i = heappop(returns)
        heappush(line, i)
    if line:
        head = heappop(line)
        amount[head] += W
        heappush(returns, (T + S, head))
print(*amount, sep="\n")
