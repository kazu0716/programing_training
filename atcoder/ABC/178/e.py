N = int(input())
INF = pow(10, 12)

p1, p2 = (INF, INF), (0, 0)
p3, p4 = (0, INF), (INF, 0)

for _ in range(N):
    x, y = map(int, input().split())
    if x+y < p1[0]+p1[1]:
        p1 = (x, y)
    if x+y > p2[0]+p2[1]:
        p2 = (x, y)
    if x-y > p3[0]-p3[1]:
        p3 = (x, y)
    if -x+y > -p4[0]+p4[1]:
        p4 = (x, y)

print(max(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]),
      abs(p3[0]-p4[0]+abs(p3[1]-p4[1]))))
