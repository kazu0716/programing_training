X, Y = map(int, input().split())
print("Yes" if Y - X <= 2 and X - Y <= 3 else "No")
