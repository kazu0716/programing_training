from itertools import permutations


def is_one_diff(s1, s2):
    diff = 0
    for j in range(M):
        if s1[j] != s2[j]:
            diff += 1
        if diff > 1:
            break
    return diff == 1


def is_exist(s):
    for i in range(N - 1):
        if not is_one_diff(s[i], s[i + 1]):
            return False
    return True


N, M = map(int, input().split())
S = [input() for _ in range(N)]
for t in permutations(S):
    if is_exist(t):
        print("Yes")
        exit()
print("No")
