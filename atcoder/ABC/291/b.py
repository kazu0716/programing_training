N = int(input())
X = sorted(list(map(int, input().split())))
print(sum(X[N:4 * N]) / (3 * N))
