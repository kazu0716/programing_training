A, B = map(int, input().split())
print("Yes" if abs(A - B) == 1 and B not in (4, 7) else "No")
