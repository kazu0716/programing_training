strs = input().split(",")
ans = []

for st in strs:
    s = ""
    for c in st:
        if c.islower():
            s += c.upper()
        else:
            s += c.lower()
    ans.append(s)
print(*ans, sep=",")
