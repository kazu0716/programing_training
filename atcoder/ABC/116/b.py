s = int(input())
a_set = set([s])
cur = s
for i in range(2, 1000100):
    nxt = cur / 2 if cur % 2 == 0 else 3 * cur + 1
    if nxt in a_set:
        print(i)
        exit()
    cur = nxt
    a_set.add(nxt)
