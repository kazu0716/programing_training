from collections import Counter

S = input()

ans = Counter(S)
cnt = 0

for k in ans:
    if ans[k] != 2:
        continue
    cnt += 1

if cnt == 2:
    print("Yes")
else:
    print("No")
