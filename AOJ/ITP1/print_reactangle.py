while True:
    l = list(map(int, input().split()))
    if l != [0, 0]:
        for i in range(l[0]):
            r = "".join(["#" for j in range(l[1])])
            print(r)
        print("")
    else:
        break
