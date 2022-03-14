from heapq import heappop, heappush
from typing import List


class Solution(object):
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs: List[List[int]] = []
        if len(nums1) > len(nums2):
            for pair in self.kSmallestPairs(nums2, nums1, k):
                pairs.append([pair[1], pair[0]])
            return pairs

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(min_heap, [nums1[i] + nums2[j], i, j])

        min_heap = [[nums1[0] + nums2[0], 0, 0]]
        while min_heap and len(pairs) < k:
            _, i, j = heappop(min_heap)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs


if __name__ == "__main__":
    input_list1 = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
    input_list2 = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
    k = int(input())
    sol = Solution()
    print(sol.kSmallestPairs(input_list1, input_list2, k))
