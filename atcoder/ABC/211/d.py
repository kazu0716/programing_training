from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
mod = pow(10, 9) + 7

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)


queue = deque([0])
dis, cnt = [-1] * N, [0] * N
dis[0], cnt[0] = 0, 1

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if dis[nxt] == -1:
            dis[nxt] = dis[cur] + 1
            queue.append(nxt)
            cnt[nxt] = cnt[cur]
        elif dis[nxt] == dis[cur] + 1:
            cnt[nxt] = (cnt[nxt] + cnt[cur]) % mod

print(cnt[N-1])
