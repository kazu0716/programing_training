def is_shooting(H, S, score, N):
    d = []
    for i in range(N):
        t = (score - H[i]) // S[i]
        d.append(t)

    d.sort()

    for i in range(N):
        if d[i] < i:
            return False

    return True


def main():
    N = int(input())
    H, S = [], []

    for _ in range(N):
        h, s = map(int, input().split())
        H.append(h)
        S.append(s)

    low, high = 0, pow(10, 18)

    while high > low:
        mid = (low + high) // 2

        if is_shooting(H, S, mid, N):
            high = mid
        else:
            low = mid + 1

    print(low)


if __name__ == '__main__':
    main()
