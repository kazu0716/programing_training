from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return list(set1 & set2)


if __name__ == "__main__":
    nums1 = list(map(int, input().replace("[", "").replace("]", "").split(",")))
    nums2 = list(map(int, input().replace("[", "").replace("]", "").split(",")))
    sol = Solution()
    print(sol.intersection(nums1, nums2))
