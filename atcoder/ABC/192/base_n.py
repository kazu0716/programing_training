from collections import deque


def base10_from(num, base):
    i, s, que = 0, 0, deque(list(str(num)))
    while que:
        s += int(que.pop()) * base ** i
        i += 1
    return s


def binary_search(x, m, d):
    if len(x) == 1:
        if int(x) > m:
            return 0
        else:
            return 1

    low = d
    high = m + 1

    while high - low > 1:
        mid = (low + high) // 2
        guess = base10_from(x, mid)
        if guess > m:
            high = mid
        else:
            low = mid
    return low - d


def main():
    X, M = input(), int(input())
    d = max(list(map(int, list(X))))
    print(binary_search(X, M, d))


if __name__ == '__main__':
    main()
