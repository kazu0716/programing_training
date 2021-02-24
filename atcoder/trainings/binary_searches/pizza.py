def binary_search(_list, item):
    low = 0
    high = len(_list) - 1

    while high >= low:
        mid = (low + high) // 2
        guess = _list[mid]

        if guess <= item and _list[mid+1] >= item:
            return min(abs(guess - item), abs(_list[mid+1] - item))
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return 0


def main():
    d, n, m = int(input()), int(input()), int(input())
    D, K = [int(input()) for _ in range(n-1)], [int(input()) for _ in range(m)]

    D.append(0)
    D.append(d)
    D.sort()

    ans = 0

    for k in K:
        ans += binary_search(D, k)

    print(ans)


if __name__ == '__main__':
    main()
