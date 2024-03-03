from typing import List, Tuple

INITIAL_VAL = (0, 0, 0, 0)


def seg_func(
    x: Tuple[int, int, int, int], y: Tuple[int, int, int, int]
) -> Tuple[int, int, int, int]:
    """
    Change function for each issues appropriately

    Pursue to be fast in this function for ABC343-F,
    because I couldn't pass the test as followings:

    cnt: Dict[int, int] = defaultdict(int)
    for k, v in ((a, s), (b, t), (c, u), (d, v)):
        cnt[k] += v
    sorted_list = sorted(list([k for k in cnt.keys()]))
    if len(sorted_list) >= 2:
        return (
            sorted_list[-1],
            sorted_list[-2],
            cnt[sorted_list[-1]],
            cnt[sorted_list[-2]],
        )
    return (sorted_list[-1], 0, cnt[sorted_list[-1]], 0)
    """
    a, b, s, t = x
    c, d, u, v = y
    if a > c:
        if b > c:
            return a, b, s, t
        if c > b:
            return a, c, s, u
        return a, b, s, t + u
    if c > a:
        if d > a:
            return c, d, u, v
        if a > d:
            return c, a, u, s
        return c, d, u, s + v
    if b > d:
        return a, b, s + u, t
    if d > b:
        return a, d, s + u, v
    return a, b, s + u, t + v


class SegTree(object):
    def __init__(self, lis: List[int]):
        # NOTE: size of list
        self.n = len(lis)
        # NOTE: min number of 2^(self.log) >= n
        self.log = (self.n - 1).bit_length()
        # NOTE: size of leaf nodes(= pow(2, self.log))
        self.size = 1 << self.log
        # NOTE: size of tree node become 2 * size
        # self.tree = [maximum value, second largest value, number of maximum values, number of second largest values]
        self.tree: List[Tuple[int, int, int, int]] = [INITIAL_VAL] * (2 * self.size)
        # NOTE: set values against leaf nodes
        for i in range(self.n):
            self.tree[self.size + i] = (lis[i], 0, 1, 0)
        # NOTE: update parent nodes from nearest each leaf node
        for i in range(self.size - 1, 0, -1):
            # NOTE: this is similar to as followings:
            # self.tree[i] = seg_func(self.tree[2 * i], self.tree[2 * i + 1])
            self.tree[i] = seg_func(self.tree[i << 1], self.tree[i << 1 | 1])

    def set(self, idx, val) -> None:
        # assert 0 <= idx < self.n
        # NOTE: move to the leaf node
        idx += self.size
        self.tree[idx] = (val, 0, 1, 0)
        # NOTE: update parent nodes
        while idx:
            self.tree[idx >> 1] = seg_func(self.tree[idx], self.tree[idx ^ 1])
            idx >>= 1

    def query(self, left, right) -> Tuple[int, int, int, int]:
        # assert 0 <= left <= right <= self.n
        # NOTE: move to parent nodes
        left += self.size
        right += self.size
        # NOTE: set default values as result of this function
        ret = INITIAL_VAL
        while left < right:
            if left & 1:
                ret = seg_func(ret, self.tree[left])
                left += 1
            if right & 1:
                ret = seg_func(ret, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return ret


N, Q = map(int, input().split())
A = list(map(int, input().split()))
seg = SegTree(A)
ans = []
for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1:]
        seg.set(p - 1, x)
    else:
        l, r = query[1:]
        # NOTE: evaluate the interval of [l - 1, r - 1) by seg.query
        ans.append(seg.query(l - 1, r)[-1])
print(*ans, sep="\n")
