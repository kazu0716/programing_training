from collections import deque

H, W = map(int, input().split())
not_visited = set()
for i in range(H):
    S = input()
    for j, s in enumerate(S):
        if s == "#":
            not_visited.add((i, j))
ans = 0
while not_visited:
    deq = deque([not_visited.pop()])
    while deq:
        cur_i, cur_j = deq.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            next_i, next_j = cur_i + di, cur_j + dj
            if 0 <= next_i < H and 0 <= next_j < W and (next_i, next_j) in not_visited:
                not_visited.remove((next_i, next_j))
                deq.append((next_i, next_j))
    ans += 1
print(ans)
