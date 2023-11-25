_, L, R = map(int, input().split())
A = list(map(int, input().split()))
print(*[min(max(a, L), R) for a in A])
