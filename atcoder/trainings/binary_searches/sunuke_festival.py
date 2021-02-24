def search_a(_list, item):
    low, high = 0, len(_list) - 1

    while high >= low:
        mid = (low + high) // 2
        guess_1 = _list[mid]
        guess_2 = _list[mid+1]

        if guess_1 < item and item <= guess_2:
            return mid
        if guess_1 >= item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search_c(_list, item):
    low, high = 0, len(_list) - 1

    while high >= low:
        mid = (low + high) // 2
        guess_1 = _list[mid]
        guess_2 = _list[mid + 1]

        if guess_1 <= item and item < guess_2:
            return mid+1
        if guess_1 > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    N = int(input())
    A, B, C = list(map(int, input().split())), list(
        map(int, input().split())), list(map(int, input().split()))

    A.append(0)
    A.append(pow(10, 10))
    A.sort()

    C.append(0)
    C.append(pow(10, 10))
    C.sort()

    ans = 0

    for b in B:
        idx_a = search_a(A, b)
        idx_c = search_c(C, b)
        ans += idx_a * (N + 1 - idx_c)

    print(ans)


if __name__ == '__main__':
    main()
