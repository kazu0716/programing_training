S = input()
T = input()

s_list, t_list = [], []
for U, L in ((S, s_list), (T, t_list)):
    for u in U:
        if not L or L[-1][0] != u:
            L.append([u, 1])
        else:
            L[-1][1] += 1
if len(s_list) != len(t_list):
    print("No")
    exit()
for i in range(len(s_list)):
    s, t = s_list[i], t_list[i]
    if s[0] != t[0] or t[1] < s[1] or (s[1] < t[1] and s[1] < 2):
        print("No")
        exit()
print("Yes")
