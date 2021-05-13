def score(l):
    s = 0
    for n in range(1, 10):
        if n in l:
            s += n * pow(10, l.count(n))
        else:
            s += n
    return s


def main():
    K = int(input())
    S, T = list(map(int, list(input()[:4]))), list(map(int, list(input()[:4])))

    cnt = 0
    range_ = range(1, 10)

    for i in range_:
        s = S[:]
        s.append(i)
        for j in range_:
            t = T[:]
            t.append(j)

            x = K - S.count(i) - T.count(i)
            y = K - S.count(j) - T.count(j)

            if score(s) > score(t) and x > 0 and y > 0:
                if i == j:
                    cnt += x * (x - 1)
                else:
                    cnt += x * y

    N = 9*K - 8
    ans = cnt / (N * (N - 1))
    print(ans)


if __name__ == '__main__':
    main()
