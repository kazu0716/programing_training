S = input()
ACGT = ("A", "C", "G", "T")
cnt, ans = 0, 0
for s in S:
    if s in ACGT:
        cnt += 1
        continue
    ans = max(ans, cnt)
    cnt = 0
print(max(ans, cnt))
