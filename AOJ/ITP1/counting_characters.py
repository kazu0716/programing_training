txt = ""
alphabets = "abcdefghijklmnopqrstuvwxyz"

while True:
    try:
        txt += input().lower()
    except EOFError:
        break

ans = [txt.count(c) for c in alphabets]

for i in range(len(alphabets)):
    print("{} : {}".format(alphabets[i], ans[i]))
