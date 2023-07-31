N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x) + 1, input().split()))
print(sorted(A + B)[M - 1])
