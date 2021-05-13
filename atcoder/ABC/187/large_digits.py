A, B = input().split()
a, b = tuple(map(int, list(A))), tuple(map(int, list(B)))
print(max(sum(a), sum(b)))
