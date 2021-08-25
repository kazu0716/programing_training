import sys

sys.setrecursionlimit(pow(10, 9))
H = int(input())


def attack(i):
    if i == 1:
        return 1
    else:
        return 2 * attack(int(i/2)) + 1


print(attack(H))
