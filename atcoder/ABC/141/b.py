S = input()
flag = True

for i in range(len(S)):
    s = S[i]
    if i % 2 == 0 and s in ("R", "U", "D") or i % 2 != 0 and s in ("L", "U", "D"):
        continue
    flag = False
    break

if flag:
    print("Yes")
else:
    print("No")
