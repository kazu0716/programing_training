S = input()
T = input()
s_set = [set([]) for _ in range(26)]
t_set = [set([]) for _ in range(26)]
for i, s in enumerate(S):
    s_set[ord(s) - 97].add(i)
for i, t in enumerate(T):
    t_set[ord(t) - 97].add(i)
for s in s_set:
    if s not in t_set:
        print("No")
        exit()
print("Yes")
