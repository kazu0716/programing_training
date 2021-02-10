while True:
    l = input().split()
    a = int(l[0])
    b = int(l[2])
    op = l[1]

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
    else:
        break
