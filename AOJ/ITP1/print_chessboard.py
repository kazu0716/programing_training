while True:
    l = list(map(int, input().split()))
    if l != [0, 0]:
        for i in range(l[0]):
            if i % 2 == 0:
                print("".join(["#" if j % 2 == 0 else "." for j in range(l[1])]))
            else:
                print("".join(["." if j % 2 == 0 else "#" for j in range(l[1])]))
        print("")
    else:
        break
