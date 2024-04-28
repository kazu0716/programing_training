A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
print((sum(A) - sum(B) + 1) if sum(A) >= sum(B) else 0)
