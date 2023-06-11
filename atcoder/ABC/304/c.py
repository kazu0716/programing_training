from collections import deque

N, D = map(int, input().split())
D2 = D ** 2
points = [tuple(map(int, input().split())) for _ in range(N)]
dis = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        d2 = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        dis[i][j] = dis[j][i] = d2
is_infection = ["No"] * N
is_infection[0] = "Yes"
deq = deque([0])
while deq:
    i = deq.popleft()
    for j in range(N):
        if dis[i][j] <= D2 and is_infection[j] == "No":
            deq.append(j)
            is_infection[j] = "Yes"
print(*is_infection, sep="\n")
