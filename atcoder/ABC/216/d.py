N, M = map(int, input().split())

tube, on_top = [], [[] for _ in range(N)]
cnt = 0
que = []

for i in range(M):
    _ = int(input())
    tube.append(list(map(int, input().split()))[::-1])
    color = tube[i][-1] - 1
    on_top[color].append(i)
    if len(on_top[color]) > 1:
        que.append(color)

while que:
    color = que.pop()
    idx1, idx2 = on_top[color]
    for idx in (idx1, idx2):
        tube[idx].pop()
        if tube[idx]:
            c = tube[idx][-1] - 1
            on_top[c].append(idx)
            if len(on_top[c]) > 1:
                que.append(c)
    cnt += 1

if cnt == N:
    print("Yes")
else:
    print("No")
