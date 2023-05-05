N, A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
mi = min(A, B, C, D, E)
# NOTE: do ceil
print(4 + (N + mi - 1) // mi)
