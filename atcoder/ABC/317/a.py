_, H, X = map(int, input().split())
P = list(map(int, input().split()))
for i, p in enumerate(P):
    if p + H >= X:
        break
print(i + 1)
