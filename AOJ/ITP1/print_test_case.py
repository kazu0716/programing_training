l = []

while True:
    n = input()
    if n == "0":
        break
    l.append(n)

for i in range(len(l)):
    print("Case {}: {}".format(i+1, l[i]))
