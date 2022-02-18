from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.nums = sorted(nums)
        heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        """
        use heapq
        """
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]

    # def add(self, val: int) -> int:
    #     """
    #     use bisect and insert
    #     """
    #     from bisect import insort_left
    #     insort_left(self.nums, val)
    #     return self.nums[-self.k]


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    for val in (3, 5, 10, 9, 4):
        print(obj.add(val))
