def id_to_int(s):
    num = 0
    for i, ss in enumerate(s[::-1]):
        num += (ord(ss) - ord("A") + 1) * pow(26, i)
    return num


S = input()
print(id_to_int(S))
