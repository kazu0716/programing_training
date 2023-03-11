from collections import deque

H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]
deq = deque([(0, 0, frozenset([A[0][0]]))])
ans = 0
while deq:
    cur_h, cur_w, path_set = deq.popleft()
    if cur_h == H - 1 and cur_w == W - 1:
        ans += 1
        continue
    for dh, dw in ((1, 0), (0, 1)):
        nxt_h, nxt_w = cur_h + dh, cur_w + dw
        if 0 <= nxt_h < H and 0 <= nxt_w < W and A[nxt_h][nxt_w] not in path_set:
            tmp_set = set(path_set.copy())
            tmp_set.add(A[nxt_h][nxt_w])
            deq.append((nxt_h, nxt_w, frozenset(tmp_set)))
print(ans)
