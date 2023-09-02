N, M, P = map(int, input().split())
print(max((N - M) // P + 1, 0))
