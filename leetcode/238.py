from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        s, cnt, idx = 1, 0, -1
        for i, num in enumerate(nums):
            if num == 0:
                cnt += 1
                idx = i
            else:
                s *= num
            if cnt > 1:
                return [0]*len(nums)
        for i in range(len(nums)):
            nums[i] = s//nums[i] if cnt == 0 else s if i == idx else 0
        return nums


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))
