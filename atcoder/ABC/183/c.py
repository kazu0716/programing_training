from itertools import permutations

N, K = map(int, input().split())
T = [[0]*N for _ in range(N)]

for i in range(N):
    t = tuple(map(int, input().split()))
    for j, t_ in enumerate(t):
        T[i][j] = t_

ans = 0

for p in permutations(range(2, N+1)):
    c = 0
    p_ = list(p)
    p_.insert(0, 1)
    p_.append(1)

    for i in range(1, N+1):
        idx1, idx2 = p_[i-1]-1, p_[i]-1
        c += T[idx1][idx2]

    if c == K:
        ans += 1

print(ans)
