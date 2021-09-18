S1, S2, S3 = input(), input(), input()
T = input()

ans = []

for t in T:
    if t == "1":
        ans.append(S1)
    elif t == "2":
        ans.append(S2)
    else:
        ans.append(S3)

print(*ans, sep="")
