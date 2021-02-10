ans = []
cards = ""

while True:
    s = input()
    if s.isalpha() or s == "-":
        if cards != "":
            ans.append(cards)
        if s == "-":
            break
        cards = s
    else:
        m = int(s)
        for _ in range(m):
            n = int(input())
            cards = cards[n:] + cards[0:n]
print(*ans, sep="\n")
