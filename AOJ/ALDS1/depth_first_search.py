from collections import deque

n = int(input())
graph = {i: deque() for i in range(n)}

for _ in range(n):
    # ref: https://note.nkmk.me/python-multi-variables-values/
    u, k, *v = map(int, input().split())
    for v_ in v:
        graph[u-1].append(v_-1)

stack, time = [], 0
seen, seen_time, done_time = [False]*n, [0]*n, [0]*n


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

        next = graph[s].popleft()
        if seen[next]:
            continue
        seen[next] = True
        stack.append(next)
        time += 1
        seen_time[next] = time


for i in range(n):
    if not seen[i]:
        dfs(i)

for u, st, dt in zip(range(n), seen_time, done_time):
    print(u+1, st, dt)
