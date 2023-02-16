from collections import defaultdict

N, Q = map(int, input().split())
connections = defaultdict(set)
ans = []
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        connections[A].add(B)
    elif T == 2:
        connections[A].discard(B)
    else:
        ans.append("Yes" if B in connections[A] and A in connections[B] else "No")
print(*ans, sep="\n")
