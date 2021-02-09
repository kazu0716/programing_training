from time import time

t1 = time()
lines = []

# TODO: 入力が上手くいかないが、countできてるので飛ばす
while True:
    line = input().lower()
    lines.append(line)
    t2 = time()
    if t2 - t1 >= 0.5:
        break

alphabets = "abcdefghijklmnopqrstuvwxyz"

ans = [" ".join(lines).count(c) for c in alphabets]

for i in range(len(alphabets)):
    print("{} : {}".format(alphabets[i], ans[i]))
