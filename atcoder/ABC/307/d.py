from collections import defaultdict

_ = input()
S = input()
string_dict = defaultdict(list)
pos = 0
for s in S:
    if "(" == s:
        pos += 1
        string_dict[pos].append(s)
    elif ")" == s and string_dict[pos] and string_dict[pos][0] == "(":
        del string_dict[pos]
        pos -= 1
    else:
        string_dict[pos].append(s)
if not string_dict:
    exit(print())
ans = []
for i in range(max(string_dict) + 1):
    ans += string_dict[i]
print(*ans, sep="")
