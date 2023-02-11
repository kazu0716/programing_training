N, M = map(int, input().split())
A = set(map(int, input().split()))
B = [i + 1 for i in range(N)]
ans, tmp = [], []
for b in B:
    if b in A:
        tmp.append(b)
    else:
        ans += [b] + tmp[::-1]
        tmp = []
print(*ans)
