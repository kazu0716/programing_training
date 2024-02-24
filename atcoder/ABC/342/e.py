from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List, Tuple

N, M = map(int, input().split())
# NOTE: max arrival time is about (pow(10, 18) + pow(10, 9))
INF = pow(10, 21)
graph: List[Dict[int, List[Tuple[int, int, int, int]]]] = [
    defaultdict(list) for _ in range(N)
]
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    # NOTE: train routes are digraph.
    # In addition, I should handle having multiple routes between the same pair of stations.
    graph[B - 1][A - 1].append((l, d, k, c))
dep_times = [-1] * N
dep_times[-1] = INF
# NOTE: time is minus, because I would like to use max-heap.
heap: List[Tuple[int, int]] = [(-dep_times[-1], N - 1)]
while heap:
    arrival_time, cur = heappop(heap)
    for nxt in graph[cur]:
        for l, d, k, c in graph[cur][nxt]:
            last_dep_time = -(arrival_time + c)
            # NOTE: there is no train at the time.
            if last_dep_time < l:
                continue
            # NOTE: get the last train by min function.
            # n = min((last_dep_time - l) // d, k - 1)
            # dep_time = l + n * d
            dep_time = l + min(k - 1, (last_dep_time - l) // d) * d
            if dep_time > dep_times[nxt]:
                dep_times[nxt] = dep_time
                heappush(heap, (-dep_time, nxt))
ans = [dep_time if dep_time > -1 else "Unreachable" for dep_time in dep_times[:-1]]
print(*ans, sep="\n")
