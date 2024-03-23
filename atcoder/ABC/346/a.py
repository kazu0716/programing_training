N = int(input())
A = tuple(map(int, input().split()))
print(*[A[i] * A[i + 1] for i in range(N - 1)])
