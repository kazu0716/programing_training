N = int(input())
for i in range(N, 1000):
    str_i = str(i)
    a, b, c = int(str_i[0]), int(str_i[1]), int(str_i[2])
    if a * b == c:
        exit(print(i))
