from math import ceil, floor, sqrt


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
for i in range(floor(sqrt(mi)), ceil(sqrt(ma)) + 1):
    s = str(pow(i, 2)).rjust(N, "0")
    if counter == get_counter(s):
        ans += 1
print(ans)
