n = input()
ans = []
for nn in n:
    if nn == "1":
        ans.append("9")
    else:
        ans.append("1")
print(*ans, sep="")
