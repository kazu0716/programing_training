def is_within_limit(limit):
    cnt, line = 0, 1
    for _l in L:
        if cnt + _l > limit:
            line += 1
            cnt = 0
        # NOTE: Return False when the string is larger than limit, because it is impossible to be put in the text-box.
        if line > M or _l > limit:
            return False
        cnt += _l + 1
    return True


N, M = map(int, input().split())
L = list(map(int, input().split()))
left, right = max(L) - 1, sum(L) + N + 1
while right - left > 1:
    mid = (left + right) // 2
    if is_within_limit(mid):
        right = mid
    else:
        left = mid
print(right)
