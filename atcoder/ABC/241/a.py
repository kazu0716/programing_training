A = tuple(map(int, input().split()))
cur = 0
for _ in range(3):
    cur = A[cur]
print(cur)
