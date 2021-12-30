N = int(input())

edge = [[] for _ in range(N)]
cnt = [0] * N

for _ in range(N-1):
    A, B = map(int, input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)
    cnt[A-1] += 1
    cnt[B-1] += 1

for i, c in enumerate(cnt):
    if c > 1:
        continue
    queue, colors = [i], [None]*N
    red, blue = set([i]), set([])
    colors[i] = "red"
    while queue:
        cur = queue.pop()
        color = colors[cur]
        for nxt in edge[cur]:
            if colors[nxt] is not None:
                continue
            colors[nxt] = "blue" if color == "red" else "red"
            if colors[nxt] == "red":
                red.add(nxt)
            else:
                blue.add(nxt)
            queue.append(nxt)
    if max(len(red), len(blue)) >= N//2:
        break

ans = tuple(red) if len(red) >= len(blue) else tuple(blue)
ans = tuple(map(lambda x: x+1, ans))
print(*ans[:N//2])
