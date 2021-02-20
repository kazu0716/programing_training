X, M = input(), int(input())

d = max(list(map(int, list(X))))
ans = 0


def base10from(num, b):
    n = 0
    numlist = list(num)
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


while True:
    d += 1
    m = base10from(X, d)
    if m > M:
        break
    ans += 1

print(ans)
