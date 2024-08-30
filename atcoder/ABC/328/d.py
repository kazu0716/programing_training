S = input()
ans = []
for s in S:
    ans.append(s)
    if len(ans) >= 3 and ans[-3:] == ["A", "B", "C"]:
        for _ in range(3):
            ans.pop()
print(*ans, sep="")
