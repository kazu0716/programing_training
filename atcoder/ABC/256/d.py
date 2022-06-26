N = int(input())
S = []
for _ in range(N):
    L, R = map(int, input().split())
    S.append((L, R))
S.sort()
i = 0
while i < len(S):
    l, r = S[i]
    while i+1 < len(S) and S[i+1][0] <= r:
        r = max(r, S[i+1][1])
        i += 1
    print(l, r)
    i += 1
