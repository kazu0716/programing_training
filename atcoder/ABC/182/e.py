from bisect import bisect_left

H, W, N, M = map(int, input().split())
lights, blocks = [], []
h_blocks = [[0] for _ in range(H+1)]
w_blocks = [[0] for _ in range(W+1)]
cnt = [[False]*(W+1) for _ in range(H+1)]
ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    lights.append((A, B))

for _ in range(M):
    C, D = map(int, input().split())
    blocks.append((C, D))
    h_blocks[C].append(D)
    w_blocks[D].append(C)

for i in range(H+1):
    h_blocks[i].append(W+1)
    h_blocks[i].sort()
for i in range(W+1):
    w_blocks[i].append(H+1)
    w_blocks[i].sort()

h_finds = [[False]*(len(h_blocks[i])) for i in range(H+1)]
w_finds = [[False]*(len(w_blocks[i])) for i in range(W+1)]
for A, B in lights:
    idx1 = bisect_left(h_blocks[A], B)
    if not h_finds[A][idx1]:
        for w in range(h_blocks[A][idx1-1]+1, h_blocks[A][idx1]):
            cnt[A][w] = True
        h_finds[A][idx1] = True
    idx2 = bisect_left(w_blocks[B], A)
    if not w_finds[B][idx2]:
        for h in range(w_blocks[B][idx2-1]+1, w_blocks[B][idx2]):
            cnt[h][B] = True
        w_finds[B][idx2] = True

for C, D in blocks:
    cnt[C][D] = False

for h in range(1, H+1):
    for w in range(1, W+1):
        if cnt[h][w]:
            ans += 1

print(ans)
