S = input()


def is_kaibun(s):
    flag = True
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            flag = False
    return flag


flag1 = is_kaibun(S)
flag2 = is_kaibun(S[0:(len(S)-1)//2])
flag3 = is_kaibun(S[(len(S)+3)//2 - 1:])

if flag1 and flag2 and flag3:
    print("Yes")
else:
    print("No")
