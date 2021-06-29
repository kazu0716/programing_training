A, B, X = map(int, input().split())


def is_ok(n):
    if X >= A * n + B * len(str(n)):
        return True
    else:
        return False


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru(pow(10, 9)+1, 0))
