r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def solve1(r1, c1, r2, c2):
    if r1+c1 == r2+c2:
        return True
    elif r1-c1 == r2-c2:
        return True
    elif abs(r1-r2) + abs(c1-c2) <= 3:
        return True
    else:
        return False


def solve2(r1, c1, r2, c2):
    if (r1 + c1 + r2 + c2) % 2 == 0:
        return True
    elif abs(r1-r2) + abs(c1-c2) <= 6:
        return True
    elif abs((r1+c1) - (r2+c2)) <= 3:
        return True
    elif abs((r1-c1) - (r2-c2)) <= 3:
        return True
    else:
        return False


def solve(r1, c1, r2, c2):
    if (r1, c1) == (r2, c2):
        return 0
    if solve1(r1, c1, r2, c2):
        return 1
    if solve2(r1, c1, r2, c2):
        return 2

    return 3


print(solve(r1, c1, r2, c2))
