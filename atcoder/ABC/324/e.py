from bisect import bisect_left
from collections import defaultdict
from sys import stdin


def get_sub_string_length(s, t):
    i = cnt = 0
    for ss in s:
        if i >= len(t):
            return cnt
        if ss == t[i]:
            cnt += 1
            i += 1
    return cnt


def main():
    N, T = stdin.readline().split()
    rev_T = T[::-1]
    prefixes, suffixes = defaultdict(int), []
    for _ in range(int(N)):
        S = stdin.readline()
        prefixes[get_sub_string_length(S, T)] += 1
        suffixes.append(get_sub_string_length(S[::-1], rev_T))
    suffixes.sort()
    ans = 0
    for prefix in prefixes:
        ans += (len(suffixes) - bisect_left(suffixes, len(T) - prefix)) * prefixes[prefix]
    print(ans)


if "__main__" == __name__:
    main()
