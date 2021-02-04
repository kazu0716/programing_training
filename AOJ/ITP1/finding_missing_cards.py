n = int(input())
cards = [[str(j) for j in range(1, 14)] for i in range(4)]

for i in range(n):
    c = input().split()
    if c[0] == "S":
        cards[0].remove(c[1])
    elif c[0] == "H":
        cards[1].remove(c[1])
    elif c[0] == "C":
        cards[2].remove(c[1])
    else:
        cards[3].remove(c[1])

for s in cards[0]:
    print("S " + s)
for h in cards[1]:
    print("H " + h)
for c in cards[2]:
    print("C " + c)
for d in cards[3]:
    print("D " + d)