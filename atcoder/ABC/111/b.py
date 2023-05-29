N = int(input())
for s_i in "123456789":
    i = int(s_i * 3)
    if N <= i:
        print(i)
        exit()
