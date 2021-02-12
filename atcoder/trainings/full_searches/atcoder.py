S = list(input())
ans, count = 0, 0

for c in S:
    if c in ("A", "C", "G", "T"):
        count += 1
    else:
        count = 0
    ans = max(ans, count)

print(ans)
