N = int(input())
st1, st2, flag = set(), set(), True

for _ in range(N):
    s = input()
    if s[0:1] == "!":
        if s[1:] in st1:
            print(s[1:])
            flag = False
            break
        else:
            st2.add(s[1:])
    else:
        if s in st2:
            print(s)
            flag = False
            break
        else:
            st1.add(s)

if flag:
    print("satisfiable")
