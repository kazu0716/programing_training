while True:
    l = list(map(int, input().split()))
    if l != [0, 0]:
        for i in range(l[0]):
            if i == 0 or i == l[0] - 1:
                print("".join(["#" for j in range(l[1])]))
            else:
                print("#" + "".join(["." for j in range(l[1]-2)]) + "#")
        print("")
    else:
        break
