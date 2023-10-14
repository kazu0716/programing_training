from math import sqrt


def get_counter(s):
    cnt = [0] * 10
    for ss in s:
        cnt[int(ss)] += 1
    return cnt


N = int(input())
S = input()
mi, ma = int("".join(sorted(list(S)))), int("".join(sorted(list(S), reverse=True)))
counter = get_counter(S)
ans = 0
i = max(int(sqrt(mi)) - 1, 0)
while i ** 2 <= ma:
    if counter == get_counter(str(i ** 2).rjust(N, "0")):
        ans += 1
    i += 1
print(ans)
