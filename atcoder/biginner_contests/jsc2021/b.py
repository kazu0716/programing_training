N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

for a in A:
    if a not in B:
        ans.append(a)

for b in B:
    if b not in A:
        ans.append(b)

ans.sort()
print(*ans)
