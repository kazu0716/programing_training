from itertools import combinations_with_replacement as cwr

N, M, Q = map(int, input().split())
req = [list(map(int, input().split())) for _ in range(Q)]

ans = 0

for seq in cwr(range(1, M+1), N):
    s = 0
    for a, b, c, d in req:
        if seq[b-1] - seq[a-1] == c:
            s += d
    ans = max(ans, s)

print(ans)
