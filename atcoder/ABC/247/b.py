N = int(input())
name = []
for _ in range(N):
    s, t = input().split()
    name.append((s, t))
for i in range(N):
    s1, t1 = name[i]
    is_s1, is_t1 = True, True
    for s2, t2 in name[:i] + name[i+1:]:
        if s1 == s2 or s1 == t2:
            is_s1 = False
        if t1 == s2 or t1 == t2:
            is_t1 = False
    if not is_s1 and not is_t1:
        print("No")
        exit()
print("Yes")
