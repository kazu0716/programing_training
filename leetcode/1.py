from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic: Dict[int, int] = {}
        for i, n in enumerate(nums):
            key = target-n
            if key in dic:
                return [i, dic[key]]
            else:
                dic[n] = i
        return [-1, -1]


if __name__ == "__main__":
    nums = list(map(int, input().replace("[", "").replace("]", "").split(",")))
    target = int(input())
    sol = Solution()
    print(sol.twoSum(nums, target))
