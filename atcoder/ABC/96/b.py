A, B, C = map(int, input().split())
K = int(input())
mx = max(A, B, C)
for _ in range(K):
    mx *= 2
print(mx + sum((A, B, C)) - max(A, B, C))
