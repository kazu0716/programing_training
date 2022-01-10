N, K = map(int, input().split())
P = list(map(int, input().split()))
S = [i for i in range(1, N+1)]

idx, s = -K, set([])
ans = [S[idx]]
for i in range(N-1, K-1, -1):
    if P[i] >= S[idx]:
        idx -= 1
    while S[idx] in s:
        idx -= 1
    s.add(P[i])
    ans.append(S[idx])

print(*ans[::-1], sep="\n")
