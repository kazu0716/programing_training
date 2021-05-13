from collections import deque

N = int(input())
C = tuple(map(int, input().split()))

graph = {i: deque() for i in range(N)}
c_dict = {C[i]: 0 for i in range(N)}

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

stack, seen, ans = [], [False]*N, []


def check(c):
    if c_dict[C[c]] == 1:
        ans.append(c)


def dfs(i):
    seen[i] = True
    stack.append(i)
    c_dict[C[i]] += 1
    check(i)

    while stack:
        s = stack[-1]
        if not graph[s]:
            p = stack.pop()
            c_dict[C[p]] -= 1
            continue

        next = graph[s].popleft()
        if seen[next]:
            continue
        seen[next] = True
        stack.append(next)
        c_dict[C[next]] += 1
        check(next)


for i in range(N):
    if not seen[i]:
        dfs(i)

ans.sort()
for a in ans:
    print(a+1)
