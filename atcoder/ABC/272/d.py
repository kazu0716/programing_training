from collections import defaultdict, deque

N, M = map(int, input().split())
i, square_dict = 0, defaultdict(int)
while i**2 <= M:
    square_dict[i**2] = i
    i += 1
dis = [[-1]*N for _ in range(N)]
dis[0][0] = 0
deq = deque([(0, 0, 0)])
while deq:
    i, j, cnt = deq.popleft()
    for k in range(N):
        square = M - (i-k) ** 2
        if square not in square_dict:
            continue
        for l in (j - square_dict[square], j + square_dict[square]):
            if 0 <= l <= N - 1 and (dis[k][l] == -1 or dis[k][l] > cnt + 1):
                dis[k][l] = cnt + 1
                deq.append((k, l, cnt + 1))
for d in dis:
    print(*d)
