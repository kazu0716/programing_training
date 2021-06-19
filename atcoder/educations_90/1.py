N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def is_ok(d):
    mid, cnt = 0, 0
    for a in A:
        if a-mid >= d:
            mid = a
            cnt += 1
        if cnt == K and L-a >= d:
            return True

    return False


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru(L, 0))
