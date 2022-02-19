from typing import List, Tuple


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans: List[Tuple[int, int]] = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                if i < len(nums1)-1 and nums1[i+1] + nums2[j] < s:
                    continue
                if len(ans) == k:
                    return sorted(ans, key=lambda x: x[0]+x[1])
                ans.append((nums1[i], nums2[j]))


if __name__ == "__main__":
    pass
