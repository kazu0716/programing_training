from collections import deque

routes = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = []

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        print(*ans, sep="\n")
        break
    dp = [[False]*W for _ in range(H)]
    fields = [[True]*W for _ in range(H)]
    queue = deque([])
    for i in range(H):
        for j, v in enumerate(list(input())):
            if v == "#":
                fields[i][j] = False
            elif v == "@":
                queue.append((i, j))
                dp[i][j] = True
    while queue:
        cur_h, cur_w = queue.popleft()
        for nxt_h, nxt_w in routes:
            nxt_h += cur_h
            nxt_w += cur_w
            if nxt_h < 0 or nxt_h >= H or nxt_w < 0 or nxt_w >= W:
                continue
            if not fields[nxt_h][nxt_w] or dp[nxt_h][nxt_w]:
                continue
            queue.append((nxt_h, nxt_w))
            dp[nxt_h][nxt_w] = True

    cnt = 0
    for i in range(H):
        for j in range(W):
            if dp[i][j]:
                cnt += 1
    ans.append(cnt)
