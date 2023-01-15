edge = [[2 * (i + 1), 2 * (i + 1) + 1] for i in range(15)]
a, b = map(int, input().split())
print("Yes" if b in edge[a - 1] else "No")
