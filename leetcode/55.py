from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = reach = 0
        while reach < len(nums) - 1:
            reach = max(reach, i + nums[i])
            if i == reach and reach < len(nums) - 1:
                return False
            i += 1
        return True


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 0, 4]
    print(sol.canJump(nums))
