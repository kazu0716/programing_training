X, M = input(), int(input())

d = max(list(map(int, list(X))))


def base10from(num, b):
    n = 0
    numlist = list(num)
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n


def binary_search(x, m, _d):
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0

    low = _d
    high = m + 1

    while high - low > 1:
        mid = (low + high) // 2
        guess = base10from(x, mid)

        if guess > m:
            high = mid
        else:
            low = mid
    return low - _d


print(binary_search(X, M, d))
