N, A, B = map(int, input().split())
C = tuple(map(int, input().split()))
print(C.index(A + B) + 1)
