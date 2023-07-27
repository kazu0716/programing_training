A, B, C, X, Y = map(int, input().split())
print(min([
    A * X + B * Y,
    C * 2 * max(X, Y),
    C * 2 * min(X, Y) + A * max((X - min(X, Y)), 0) + B * max((Y - min(X, Y)), 0)
]))
