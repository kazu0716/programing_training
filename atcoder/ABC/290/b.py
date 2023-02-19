N, K = map(int, input().split())
S = input()
ans = []
for s in S:
    if K > 0 and s == "o":
        ans.append("o")
        K -= 1
    else:
        ans.append("x")
print(*ans, sep="")
