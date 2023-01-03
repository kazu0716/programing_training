N = int(input())
S = input()
is_surrounded = False
ans = []
for s in S:
    if s == '"':
        is_surrounded = not is_surrounded
    elif s == "," and not is_surrounded:
        s = "."
    ans.append(s)
print(*ans, sep="")
