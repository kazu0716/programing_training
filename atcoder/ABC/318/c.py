N, D, P = map(int, input().split())
F = list(map(int, input().split()))
target = P / D
cnt = 0
for f in F:
    if f >= target:
        cnt += 1
ans = []
for tickets in (cnt // D, cnt // D + 1):
    sorted_F = sorted(F)
    for _ in range(tickets * D):
        if sorted_F:
            sorted_F.pop()
    ans.append(P * tickets + sum(sorted_F))
print(min(ans))
