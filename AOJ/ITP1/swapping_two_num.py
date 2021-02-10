l = []

while True:
    n = sorted(list(map(int, input().split())))
    if n == [0, 0]:
        break
    n.sort()
    l.append(n)

for i in l:
    print("{} {}".format(i[0], i[1]))
