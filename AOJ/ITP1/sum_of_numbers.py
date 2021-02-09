def main():
    strs = []

    while True:
        ns = input()
        if int(ns) == 0:
            break
        strs.append(list(map(int, list(ns))))

    for s in strs:
        print(sum(s))


if __name__ == "__main__":
    main()
