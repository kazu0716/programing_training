S = input()

used = S.count("o")

ans = 0
for i in range(10000):
    passwd = str(i).rjust(4, "0")
    cnt, flag = [False]*10, True
    for j in range(4):
        k = int(passwd[j])
        if S[k] == "o":
            cnt[k] = True
        elif S[k] == "x":
            flag = False
    if cnt.count(True) == used and flag:
        ans += 1
print(ans)
