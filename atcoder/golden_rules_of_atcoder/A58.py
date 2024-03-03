# ref: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bf
from typing import List

INITIAL = -pow(10, 9)


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
        self.tree: List[int] = [INITIAL] * (2 * self.size)
        # NOTE: set values against leaf nodes
        for i in range(self.n):
            self.tree[self.size + i] = lis[i]
        # NOTE: update parent nodes from nearest each leaf node
        for i in range(self.size - 1, 0, -1):
            # NOTE: this is similar to as followings:
            # self.tree[i] = seg_func(self.tree[2 * i], self.tree[2 * i + 1])
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def set(self, idx, val) -> None:
        # assert 0 <= idx < self.n
        # NOTE: move to the leaf node
        idx += self.size
        self.tree[idx] = val
        # NOTE: update parent nodes
        while idx:
            self.tree[idx >> 1] = max(self.tree[idx], self.tree[idx ^ 1])
            idx >>= 1

    def query(self, left, right) -> int:
        # assert 0 <= left <= right <= self.n
        # NOTE: move to parent nodes
        left += self.size
        right += self.size
        # NOTE: set default values as result of this function
        ret = INITIAL
        while left < right:
            if left & 1:
                ret = max(ret, self.tree[left])
                left += 1
            if right & 1:
                ret = max(ret, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return ret


N, Q = map(int, input().split())
A = [0] * N
seg_tree = SegTree(A)
ans = []
for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        pos, x = query[1:]
        seg_tree.set(pos - 1, x)
    else:
        l, r = query[1:]
        ans.append(seg_tree.query(l - 1, r - 1))
print(*ans, sep="\n")
