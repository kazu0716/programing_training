from bisect import bisect_right

N, K = map(int, input().split())
P = []

for _ in range(N):
    p1, p2, p3 = map(int, input().split())
    P.append(p1+p2+p3)

S = sorted(P)
ans = []
for p in P:
    p += 300
    idx = bisect_right(S, p)
    if idx == N:
        rank = 1
    elif p == S[idx]:
        rank = N - idx
    else:
        rank = N - idx + 1

    if rank <= K:
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")
