from bisect import bisect_left

_, _, N = map(int, input().split())

x_list, y_list = [], []
points = []

for _ in range(N):
    A, B = map(int, input().split())
    x_list.append(A)
    y_list.append(B)
    points.append([A, B])

x_list.sort()
y_list.sort()
x_list = list(set(x_list))
y_list = list(set(y_list))

for i in range(len(points)):
    x, y = points[i][0], points[i][1]
    idx_x = bisect_left(x_list, x) + 1
    idx_y = bisect_left(y_list, y) + 1
    print(idx_x, idx_y)
