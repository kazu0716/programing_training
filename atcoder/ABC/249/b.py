S = input()
is_lower, is_upper = False, False
s_set = set()
for s in S:
    if s in s_set:
        print("No")
        exit()
    s_set.add(s)
    if s.islower():
        is_lower = True
    if s.isupper():
        is_upper = True
if is_lower and is_upper:
    print("Yes")
else:
    print("No")
