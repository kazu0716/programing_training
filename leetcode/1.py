from itertools import combinations


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, idx2 in combinations(range(len(nums)), 2):
            if nums[idx1] + nums[idx2] == target:
                return [idx1, idx2]
        return []
