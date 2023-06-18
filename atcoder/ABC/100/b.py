D, N = map(int, input().split())
print(pow(100, D) * (N if N < 100 else N + 1))
