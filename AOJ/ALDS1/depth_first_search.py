import collections

n = int(input())
graph = {i: collections.deque() for i in range(n)}

for _ in range(n):
    u, k, *v = map(int, input().split())
    for v_ in v:
        graph[u-1].append(v_-1)

seen = [False]*n
stack = []
time = 0
seen_time = [0]*n
done_time = [0]*n


def dfs(i):
    global time

    seen[i] = True
    stack.append(i)
    time += 1
    seen_time[i] = time

    while stack:
        s = stack[-1]
        if not graph[s]:
            stack.pop()
            time += 1
            done_time[s] = time
            continue

        t = graph[s].popleft()
        if seen[t]:
            continue
        seen[t] = True
        stack.append(t)
        time += 1
        seen_time[t] = time


for i in range(n):
    if not seen[i]:
        dfs(i)

for u, st, dt in zip(range(n), seen_time, done_time):
    print(u+1, st, dt)
