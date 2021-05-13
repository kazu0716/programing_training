from itertools import combinations, permutations
from sys import stdin


def to_i(dic, s):
    n = 0
    for c in s:
        n = n * 10 + dic[c]
    return n


def solve(s1, s2, s3):
    uni_w = set(s1+s2+s3)

    if len(uni_w) > 10:
        return None

    for c in combinations(range(10), len(uni_w)):
        for p in permutations(c):
            dic = {k: v for k, v in zip(uni_w, p)}

            if dic[s1[0]] == 0 or dic[s2[0]] == 0 or dic[s3[0]] == 0:
                continue

            a, b, c = to_i(dic, s1), to_i(dic, s2), to_i(dic, s3)
            if a + b == c:
                return a, b, c

    return None


def main():
    S1, S2, S3 = stdin.readline().strip(
    ), stdin.readline().strip(), stdin.readline().strip()
    ans = solve(S1, S2, S3)

    if ans is None:
        print("UNSOLVABLE")
    else:
        print(*ans, sep="\n")


if __name__ == '__main__':
    main()
