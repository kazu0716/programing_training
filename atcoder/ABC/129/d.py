from bisect import bisect_left

H, W = map(int, input().split())
points = []
h_blocks = [[0] for _ in range(H+1)]
w_blocks = [[0] for _ in range(W+1)]

for h in range(H):
    fields = input()
    for w in range(W):
        if fields[w] == ".":
            points.append((h+1, w+1))
        else:
            h_blocks[h+1].append(w+1)
            w_blocks[w+1].append(h+1)

for h in range(1, H+1):
    h_blocks[h].append(W+1)
for w in range(1, W+1):
    w_blocks[w].append(H+1)

ans = 0
for h, w in points:
    h_idx, w_idx = bisect_left(h_blocks[h], w), bisect_left(w_blocks[w], h)
    h_cnt = h_blocks[h][h_idx]-(h_blocks[h][h_idx-1]+1)
    w_cnt = w_blocks[w][w_idx]-(w_blocks[w][w_idx-1]+1)
    ans = max(ans, h_cnt+w_cnt-1)

print(ans)
